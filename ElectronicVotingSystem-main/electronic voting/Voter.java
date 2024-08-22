import java.util.UUID;

public class Voter {
    private String voterId;

    public Voter() {
        this.voterId = UUID.randomUUID().toString();
    }

    public String getVoterId() {
        return voterId;
    }
}
