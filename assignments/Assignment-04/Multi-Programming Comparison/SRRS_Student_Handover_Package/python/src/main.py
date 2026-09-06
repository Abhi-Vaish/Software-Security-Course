
from service import BookingService

def handle(service, line):
    parts = line.strip().split("|")
    if not parts or not parts[0]:
        return "ERROR|invalid_request"

    op = parts[0]
    try:
        if op == "AUTH" and len(parts) == 3:
            token, user = service.authenticate(parts[1], parts[2])
            return f"OK|TOKEN|{token}|USER|{user}"
        if op == "SEARCH" and len(parts) == 2:
            trains = service.search_train(parts[1])
            return "OK|TRAINS|" + ",".join(trains)
        if op == "SEATS" and len(parts) == 2:
            seats = service.get_available_seats(parts[1])
            return "OK|SEATS|" + ",".join(seats)
        if op == "BOOK" and len(parts) == 5:
            result = service.book_seat(parts[1], parts[2], parts[3], parts[4])
            if result[0] == "OK":
                r = result[1]
                return f"OK|RESERVATION|{r.reservation_id}|USER|{r.user_id}|TRAIN|{r.train_id}|SEAT|{r.seat_no}"
            return f"ERROR|{result[1]}"
        if op == "GET" and len(parts) == 3:
            result = service.get_reservation(parts[1], parts[2])
            if result[0] == "OK":
                r = result[1]
                return f"OK|RESERVATION|{r.reservation_id}|USER|{r.user_id}|TRAIN|{r.train_id}|SEAT|{r.seat_no}"
            return f"ERROR|{result[1]}"
        return "ERROR|invalid_request"
    except Exception:
        return "ERROR|request_failed"

if __name__ == "__main__":
    service = BookingService()
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip().upper() == "QUIT":
            break
        print(handle(service, line), flush=True)
