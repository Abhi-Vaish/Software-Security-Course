
from dataclasses import dataclass
from threading import Lock
from uuid import uuid4


@dataclass(frozen=True)
class Reservation:
    reservation_id: str
    user_id: str
    train_id: str
    seat_no: str


class IdentityService:
    def __init__(self):
        self.users = {
            "alice": ("alice123", "U100"),
            "bob": ("bob123", "U200"),
        }

    def authenticate(self, username, password):
        record = self.users.get(username)
        if record and record[0] == password:
            return record[1]
        return None


class TrainSeatService:
    def __init__(self):
        self.trains = {"T1": "Aarhus Express"}
        self.seats = {"T1": {"S1", "S2", "S3", "S4"}}
        self.lock = Lock()

    def search(self, criteria):
        return [tid for tid, name in self.trains.items()
                if criteria.lower() in tid.lower() or criteria.lower() in name.lower()]

    def available_seats(self, train_id):
        return sorted(self.seats.get(train_id, set()))

    def reserve(self, train_id, seat_no):
        # The operation is synchronized so that two threads cannot
        # successfully allocate the same seat in this implementation.
        with self.lock:
            seats = self.seats.get(train_id)
            if seats is None:
                return False
            if seat_no not in seats:
                return False
            seats.remove(seat_no)
            return True


class ReservationDatabase:
    def __init__(self):
        self.reservations = {}

    def save(self, reservation):
        self.reservations[reservation.reservation_id] = reservation

    def get(self, reservation_id):
        return self.reservations.get(reservation_id)


class BookingService:
    def __init__(self):
        self.identity = IdentityService()
        self.train_seat = TrainSeatService()
        self.db = ReservationDatabase()
        self.sessions = {}
        self.session_lock = Lock()

    def authenticate(self, username, password):
        user_id = self.identity.authenticate(username, password)
        if user_id is None:
            raise ValueError("authentication_failed")
        token = str(uuid4())
        with self.session_lock:
            self.sessions[token] = user_id
        return token, user_id

    def _authenticated_user(self, token):
        with self.session_lock:
            return self.sessions.get(token)

    def search_train(self, criteria):
        return self.train_seat.search(criteria)

    def get_available_seats(self, train_id):
        return self.train_seat.available_seats(train_id)

    def book_seat(self, token, requested_user_id, train_id, seat_no):
        user_id = self._authenticated_user(token)
        if user_id is None:
            return ("ERROR", "not_authenticated")

        # Starter implementation: ownership authorization is incomplete.
        if not self.train_seat.reserve(train_id, seat_no):
            return ("ERROR", "seat_unavailable")

        reservation = Reservation(str(uuid4()), requested_user_id, train_id, seat_no)
        self.db.save(reservation)
        return ("OK", reservation)

    def get_reservation(self, token, reservation_id):
        user_id = self._authenticated_user(token)
        if user_id is None:
            return ("ERROR", "not_authenticated")

        reservation = self.db.get(reservation_id)
        if reservation is None:
            return ("ERROR", "reservation_not_found")

        # Starter implementation: ownership authorization is incomplete.
        return ("OK", reservation)
