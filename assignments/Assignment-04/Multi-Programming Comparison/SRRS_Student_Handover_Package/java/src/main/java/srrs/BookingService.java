
package srrs;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

class Reservation {
    final String id, userId, trainId, seatNo;
    Reservation(String id, String userId, String trainId, String seatNo) {
        this.id = id; this.userId = userId; this.trainId = trainId; this.seatNo = seatNo;
    }
}

public class BookingService {
    private final Map<String, String[]> users = new HashMap<>();
    private final Map<String, String> trains = new HashMap<>();
    private final Map<String, Set<String>> seats = new HashMap<>();
    private final Map<String, String> sessions = new ConcurrentHashMap<>();
    private final Map<String, Reservation> reservations = new ConcurrentHashMap<>();

    public BookingService() {
        users.put("alice", new String[]{"alice123", "U100"});
        users.put("bob", new String[]{"bob123", "U200"});
        trains.put("T1", "Aarhus Express");
        seats.put("T1", new HashSet<>(Arrays.asList("S1","S2","S3","S4")));
    }

    public String[] authenticate(String username, String password) {
        String[] u = users.get(username);
        if (u == null || !u[0].equals(password)) throw new IllegalArgumentException();
        String token = UUID.randomUUID().toString();
        sessions.put(token, u[1]);
        return new String[]{token, u[1]};
    }

    public List<String> searchTrain(String criteria) {
        List<String> result = new ArrayList<>();
        for (Map.Entry<String,String> e : trains.entrySet()) {
            if (e.getKey().toLowerCase().contains(criteria.toLowerCase()) ||
                e.getValue().toLowerCase().contains(criteria.toLowerCase())) {
                result.add(e.getKey());
            }
        }
        Collections.sort(result);
        return result;
    }

    public List<String> availableSeats(String trainId) {
        Set<String> s = seats.get(trainId);
        if (s == null) return Collections.emptyList();
        List<String> result = new ArrayList<>(s);
        Collections.sort(result);
        return result;
    }

    public synchronized Object[] bookSeat(String token, String requestedUserId,
                                           String trainId, String seatNo) {
        if (!sessions.containsKey(token)) return new Object[]{"ERROR","not_authenticated"};
        Set<String> s = seats.get(trainId);
        if (s == null || !s.remove(seatNo)) return new Object[]{"ERROR","seat_unavailable"};

        Reservation r = new Reservation(UUID.randomUUID().toString(),
                                        requestedUserId, trainId, seatNo);
        reservations.put(r.id, r);
        return new Object[]{"OK", r};
    }

    public Object[] getReservation(String token, String reservationId) {
        if (!sessions.containsKey(token)) return new Object[]{"ERROR","not_authenticated"};
        Reservation r = reservations.get(reservationId);
        if (r == null) return new Object[]{"ERROR","reservation_not_found"};
        return new Object[]{"OK", r};
    }
}
