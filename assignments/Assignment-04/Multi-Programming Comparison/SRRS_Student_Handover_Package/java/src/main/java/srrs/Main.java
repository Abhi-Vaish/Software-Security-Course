
package srrs;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BookingService service = new BookingService();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = reader.readLine()) != null) {
            if (line.trim().equalsIgnoreCase("QUIT")) break;
            System.out.println(handle(service, line));
        }
    }

    static String handle(BookingService service, String line) {
        String[] p = line.trim().split("\\|", -1);
        if (p.length == 0) return "ERROR|invalid_request";
        try {
            switch (p[0]) {
                case "AUTH":
                    if (p.length != 3) return "ERROR|invalid_request";
                    String[] auth = service.authenticate(p[1], p[2]);
                    return "OK|TOKEN|" + auth[0] + "|USER|" + auth[1];
                case "SEARCH":
                    if (p.length != 2) return "ERROR|invalid_request";
                    return "OK|TRAINS|" + String.join(",", service.searchTrain(p[1]));
                case "SEATS":
                    if (p.length != 2) return "ERROR|invalid_request";
                    return "OK|SEATS|" + String.join(",", service.availableSeats(p[1]));
                case "BOOK":
                    if (p.length != 5) return "ERROR|invalid_request";
                    Object[] b = service.bookSeat(p[1], p[2], p[3], p[4]);
                    if (!"OK".equals(b[0])) return "ERROR|" + b[1];
                    Reservation r = (Reservation)b[1];
                    return "OK|RESERVATION|" + r.id + "|USER|" + r.userId +
                           "|TRAIN|" + r.trainId + "|SEAT|" + r.seatNo;
                case "GET":
                    if (p.length != 3) return "ERROR|invalid_request";
                    Object[] g = service.getReservation(p[1], p[2]);
                    if (!"OK".equals(g[0])) return "ERROR|" + g[1];
                    Reservation gr = (Reservation)g[1];
                    return "OK|RESERVATION|" + gr.id + "|USER|" + gr.userId +
                           "|TRAIN|" + gr.trainId + "|SEAT|" + gr.seatNo;
                default:
                    return "ERROR|invalid_request";
            }
        } catch (Exception e) {
            return "ERROR|request_failed";
        }
    }
}
