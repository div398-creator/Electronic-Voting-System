import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class VotingSystem {
    private List<Voter> voters;
    private Map<String, String> votes;

    public VotingSystem() {
        this.voters = new ArrayList<>();
        this.votes = new HashMap<>();
    }

    public void registerVoter(Voter voter) {
        voters.add(voter);
    }

    public boolean canVote(String voterId) {
        // Check if the voter is registered and hasn't already voted
        return voters.stream().anyMatch(v -> v.getVoterId().equals(voterId)) && !votes.containsKey(voterId);
    }

    public void castVote(String voterId, String candidate) throws IOException {
        if (canVote(voterId)) {
            votes.put(voterId, candidate);
            storeVote(voterId, candidate);
            System.out.println("Vote successfully cast.");
        } else {
            System.out.println("Vote rejected: Invalid voter ID or vote already cast.");
        }
    }

    private void storeVote(String voterId, String candidate) throws IOException {
        try (FileWriter writer = new FileWriter("votes.txt", true)) {
            writer.write(voterId + ":" + candidate + "\n");
        }
    }

    public Map<String, Integer> tallyVotes() throws IOException {
        Map<String, Integer> results = new HashMap<>();
        List<String> lines = Files.readAllLines(Paths.get("votes.txt"));

        for (String line : lines) {
            String[] parts = line.split(":");
            String candidate = parts[1];
            results.put(candidate, results.getOrDefault(candidate, 0) + 1);
        }

        return results;
    }

    public static void main(String[] args) throws IOException {
        VotingSystem votingSystem = new VotingSystem();
        Voter voter1 = new Voter();
        Voter voter2 = new Voter();

        votingSystem.registerVoter(voter1);
        votingSystem.registerVoter(voter2);

        Scanner scanner = new Scanner(System.in);

        // Voter 1
        System.out.println("Voter 1: Enter candidate to vote for:");
        String candidate1 = scanner.nextLine();
        votingSystem.castVote(voter1.getVoterId(), candidate1);

        // Voter 2
        System.out.println("Voter 2: Enter candidate to vote for:");
        String candidate2 = scanner.nextLine();
        votingSystem.castVote(voter2.getVoterId(), candidate2);

        // Display the results
        Map<String, Integer> results = votingSystem.tallyVotes();
        System.out.println("Voting Results: " + results);
    }
}
