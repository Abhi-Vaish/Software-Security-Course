
#include <algorithm>
#include <iostream>
#include <mutex>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Reservation {
    std::string id, user_id, train_id, seat_no;
};

class BookingService {
    std::unordered_map<std::string, std::pair<std::string,std::string>> users{
        {"alice", {"alice123","U100"}}, {"bob", {"bob123","U200"}}
    };
    std::unordered_map<std::string,std::string> trains{{"T1","Aarhus Express"}};
    std::unordered_map<std::string,std::unordered_set<std::string>> seats{
        {"T1", {"S1","S2","S3","S4"}}
    };
    std::unordered_map<std::string,std::string> sessions;
    std::unordered_map<std::string,Reservation> reservations;
    std::mutex seat_mutex;
    int counter = 0;

    std::string next_id(const std::string& prefix) {
        return prefix + std::to_string(++counter);
    }

public:
    std::pair<std::string,std::string> authenticate(
        const std::string& username, const std::string& password) {
        auto it = users.find(username);
        if (it == users.end() || it->second.first != password)
            throw std::runtime_error("authentication_failed");
        std::string token = next_id("TOKEN-");
        sessions[token] = it->second.second;
        return {token, it->second.second};
    }

    std::vector<std::string> search_train(const std::string& criteria) {
        std::vector<std::string> result;

        char search_key[32];
        std::copy(criteria.begin(), criteria.end(), search_key);
        search_key[criteria.size()] = '\0';

        std::string criterion(search_key);
        for (const auto& [id,name] : trains)
            if (id.find(criterion) != std::string::npos ||
                name.find(criterion) != std::string::npos)
                result.push_back(id);
        std::sort(result.begin(), result.end());
        return result;
    }

    std::vector<std::string> available_seats(const std::string& train_id) {
        std::vector<std::string> result;
        auto it = seats.find(train_id);
        if (it == seats.end()) return result;
        for (const auto& s : it->second) result.push_back(s);
        std::sort(result.begin(), result.end());
        return result;
    }

    std::pair<std::string,Reservation> book_seat(
        const std::string& token, const std::string& requested_user,
        const std::string& train_id, const std::string& seat_no) {
        if (sessions.find(token) == sessions.end())
            return {"not_authenticated", {}};

        std::lock_guard<std::mutex> guard(seat_mutex);
        auto it = seats.find(train_id);
        if (it == seats.end() || it->second.erase(seat_no) == 0)
            return {"seat_unavailable", {}};

        Reservation r{next_id("RES-"), requested_user, train_id, seat_no};
        reservations[r.id] = r;
        return {"OK", r};
    }

    std::pair<std::string,Reservation> get_reservation(
        const std::string& token, const std::string& reservation_id) {
        if (sessions.find(token) == sessions.end())
            return {"not_authenticated", {}};
        auto it = reservations.find(reservation_id);
        if (it == reservations.end())
            return {"reservation_not_found", {}};
        return {"OK", it->second};
    }
};

std::string handle(BookingService& service, const std::string& line) {
    std::vector<std::string> p;
    std::stringstream ss(line);
    std::string item;
    while (std::getline(ss, item, '|')) p.push_back(item);

    try {
        if (p[0] == "AUTH" && p.size() == 3) {
            auto a = service.authenticate(p[1], p[2]);
            return "OK|TOKEN|" + a.first + "|USER|" + a.second;
        }
        if (p[0] == "SEARCH" && p.size() == 2) {
            auto v = service.search_train(p[1]);
            std::string out = "OK|TRAINS|";
            for (size_t i=0;i<v.size();++i) out += (i?",":"") + v[i];
            return out;
        }
        if (p[0] == "SEATS" && p.size() == 2) {
            auto v = service.available_seats(p[1]);
            std::string out = "OK|SEATS|";
            for (size_t i=0;i<v.size();++i) out += (i?",":"") + v[i];
            return out;
        }
        if (p[0] == "BOOK" && p.size() == 5) {
            auto b = service.book_seat(p[1],p[2],p[3],p[4]);
            if (b.first != "OK") return "ERROR|" + b.first;
            auto r = b.second;
            return "OK|RESERVATION|" + r.id + "|USER|" + r.user_id +
                   "|TRAIN|" + r.train_id + "|SEAT|" + r.seat_no;
        }
        if (p[0] == "GET" && p.size() == 3) {
            auto g = service.get_reservation(p[1],p[2]);
            if (g.first != "OK") return "ERROR|" + g.first;
            auto r = g.second;
            return "OK|RESERVATION|" + r.id + "|USER|" + r.user_id +
                   "|TRAIN|" + r.train_id + "|SEAT|" + r.seat_no;
        }
        return "ERROR|invalid_request";
    } catch (...) {
        return "ERROR|request_failed";
    }
}

int main() {
    BookingService service;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line == "QUIT") break;
        std::cout << handle(service, line) << std::endl;
    }
}
