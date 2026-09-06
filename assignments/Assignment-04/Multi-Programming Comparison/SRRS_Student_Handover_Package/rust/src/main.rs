
use std::collections::{HashMap, HashSet};
use std::io::{self, BufRead};
use std::sync::{Arc, Mutex};

#[derive(Clone)]
struct Reservation {
    id: String,
    user_id: String,
    train_id: String,
    seat_no: String,
}

struct BookingService {
    users: HashMap<String, (String,String)>,
    trains: HashMap<String,String>,
    seats: Arc<Mutex<HashMap<String,HashSet<String>>>>,
    sessions: HashMap<String,String>,
    reservations: HashMap<String,Reservation>,
    counter: u64,
}

impl BookingService {
    fn new() -> Self {
        let mut users = HashMap::new();
        users.insert("alice".into(), ("alice123".into(),"U100".into()));
        users.insert("bob".into(), ("bob123".into(),"U200".into()));

        let mut trains = HashMap::new();
        trains.insert("T1".into(), "Aarhus Express".into());

        let mut all = HashSet::new();
        for s in ["S1","S2","S3","S4"] { all.insert(s.to_string()); }
        let mut seats = HashMap::new();
        seats.insert("T1".into(), all);

        Self {
            users, trains, seats: Arc::new(Mutex::new(seats)),
            sessions: HashMap::new(), reservations: HashMap::new(), counter: 0
        }
    }

    fn id(&mut self, prefix: &str) -> String {
        self.counter += 1;
        format!("{}{}", prefix, self.counter)
    }

    fn authenticate(&mut self, username: &str, password: &str)
        -> Result<(String,String), String> {
        match self.users.get(username) {
            Some((pw, uid)) if pw == password => {
                let uid2 = uid.clone();
                let token = self.id("TOKEN-");
                self.sessions.insert(token.clone(), uid2.clone());
                Ok((token, uid2))
            }
            _ => Err("authentication_failed".into())
        }
    }

    fn search_train(&self, criteria: &str) -> Vec<String> {
        let mut out = Vec::new();
        for (id, name) in &self.trains {
            if id.contains(criteria) || name.contains(criteria) {
                out.push(id.clone());
            }
        }
        out.sort();
        out
    }

    fn available_seats(&self, train_id: &str) -> Vec<String> {
        let seats = self.seats.lock().unwrap();
        let mut out = seats.get(train_id)
            .map(|s| s.iter().cloned().collect::<Vec<_>>())
            .unwrap_or_default();
        out.sort();
        out
    }

    fn book_seat(&mut self, token: &str, requested_user: &str,
                 train_id: &str, seat_no: &str) -> Result<Reservation,String> {
        if !self.sessions.contains_key(token) {
            return Err("not_authenticated".into());
        }

        // Generate the reservation ID before locking the seat store so the
        // mutable operation on self does not overlap the MutexGuard borrow.
        let id = self.id("RES-");

        let mut seats = self.seats.lock().unwrap();
        let set = match seats.get_mut(train_id) {
            Some(s) => s,
            None => return Err("seat_unavailable".into())
        };

        if !set.remove(seat_no) {
            return Err("seat_unavailable".into());
        }
        let r = Reservation {
            id: id.clone(), user_id: requested_user.to_string(),
            train_id: train_id.to_string(), seat_no: seat_no.to_string()
        };
        self.reservations.insert(id, r.clone());
        Ok(r)
    }

    fn get_reservation(&self, token: &str, reservation_id: &str)
        -> Result<Reservation,String> {
        if !self.sessions.contains_key(token) {
            return Err("not_authenticated".into());
        }
        self.reservations.get(reservation_id)
            .cloned()
            .ok_or_else(|| "reservation_not_found".into())
    }
}

fn handle(service: &mut BookingService, line: &str) -> String {
    let p: Vec<&str> = line.trim().split('|').collect();
    if p.is_empty() { return "ERROR|invalid_request".into(); }

    match p[0] {
        "AUTH" if p.len() == 3 => match service.authenticate(p[1],p[2]) {
            Ok((token,user)) => format!("OK|TOKEN|{}|USER|{}",token,user),
            Err(_) => "ERROR|authentication_failed".into()
        },
        "SEARCH" if p.len() == 2 => {
            format!("OK|TRAINS|{}", service.search_train(p[1]).join(","))
        },
        "SEATS" if p.len() == 2 => {
            format!("OK|SEATS|{}", service.available_seats(p[1]).join(","))
        },
        "BOOK" if p.len() == 5 => match service.book_seat(p[1],p[2],p[3],p[4]) {
            Ok(r) => format!("OK|RESERVATION|{}|USER|{}|TRAIN|{}|SEAT|{}",
                             r.id,r.user_id,r.train_id,r.seat_no),
            Err(e) => format!("ERROR|{}",e)
        },
        "GET" if p.len() == 3 => match service.get_reservation(p[1],p[2]) {
            Ok(r) => format!("OK|RESERVATION|{}|USER|{}|TRAIN|{}|SEAT|{}",
                             r.id,r.user_id,r.train_id,r.seat_no),
            Err(e) => format!("ERROR|{}",e)
        },
        _ => "ERROR|invalid_request".into()
    }
}

fn main() {
    let stdin = io::stdin();
    let mut service = BookingService::new();
    for line in stdin.lock().lines() {
        let line = line.unwrap();
        if line.trim() == "QUIT" { break; }
        println!("{}", handle(&mut service, &line));
    }
}
