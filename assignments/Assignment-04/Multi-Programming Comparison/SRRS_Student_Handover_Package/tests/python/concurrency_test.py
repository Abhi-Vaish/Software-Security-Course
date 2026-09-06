import threading
from src.service import BookingService


service = BookingService()

# Authenticate two users

alice_token, _ = service.authenticate("alice", "alice123")
bob_token, _ = service.authenticate("bob", "bob123")


print("Alice token:", alice_token)
print("Bob token:", bob_token)

results = []


def book_as_alice():
    result = service.book_seat(
        alice_token,
        "U100",
        "T1",
        "S4"
    )
    results.append(("Alice", result))


def book_as_bob():
    result = service.book_seat(
        bob_token,
        "U200",
        "T1",
        "S4"
    )
    results.append(("Bob", result))


# Start both booking attempts at approximately the same time
t1 = threading.Thread(target=book_as_alice)
t2 = threading.Thread(target=book_as_bob)

t1.start()
t2.start()

t1.join()
t2.join()

print("\nConcurrent booking results:")
for user, result in results:
    print(user, "->", result)