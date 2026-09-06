import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from service import BookingService


class TestBookingService(unittest.TestCase):
    def test_legitimate_booking_and_retrieval(self):
        service = BookingService()
        token, user = service.authenticate("alice", "alice123")
        result = service.book_seat(token, user, "T1", "S1")
        self.assertEqual(result[0], "OK")
        reservation = result[1]
        self.assertEqual(
            service.get_reservation(token, reservation.reservation_id)[0],
            "OK",
        )

    def test_unauthenticated_booking_is_denied(self):
        service = BookingService()
        result = service.book_seat("bad-token", "U100", "T1", "S1")
        self.assertEqual(result, ("ERROR", "not_authenticated"))


if __name__ == "__main__":
    unittest.main()
