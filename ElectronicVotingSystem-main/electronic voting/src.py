import hashlib
import random
import string
import secrets
from collections import Counter

# Function to generate a secure hash for the votes
def generate_hash(vote):
    """Generate SHA-256 hash for the given vote."""
    return hashlib.sha256(vote.encode()).hexdigest()

# Function to generate a secure, random voter ID
def generate_voter_id():
    """Generate a secure random voter ID using secrets module."""
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(12))

# Function to validate a vote
def validate_vote(vote):
    """Ensure the vote is for a valid candidate."""
    if vote in ["Candidate_A", "Candidate_B"]:
        return True
    else:
        print("Invalid vote. Please vote for a valid candidate (Candidate_A, Candidate_B).")
        return False

# Function to cast a vote
def cast_vote(voter_id, votes_db):
    """Allow a voter to cast their vote."""
    print("\nVoting Options: Candidate_A, Candidate_B")
    
    while True:
        vote = input("Enter your vote: ").strip()
        if validate_vote(vote):
            break
    
    vote_hash = generate_hash(vote)
    
    # Prevent duplicate voting
    if voter_id in votes_db:
        print(f"Voter {voter_id} has already voted! You cannot vote again.")
    else:
        votes_db[voter_id] = vote_hash
        print(f"Voter {voter_id} has successfully cast their vote.")

# Function to tally votes and determine the winner
def tally_votes(votes_db):
    """Tally votes, announce results, and declare the winner."""
    print("\nTallying votes...\n")
    tally = {"Candidate_A": 0, "Candidate_B": 0}
    
    for vote_hash in votes_db.values():
        if vote_hash == generate_hash("Candidate_A"):
            tally["Candidate_A"] += 1
        elif vote_hash == generate_hash("Candidate_B"):
            tally["Candidate_B"] += 1

    # Display the vote tally results
    for candidate, count in tally.items():
        print(f"{candidate} received {count} votes.")
    
    # Determine the winner
    winner = determine_winner(tally)
    
    if winner:
        print(f"\nThe winner of the election is: {winner}")
    else:
        print("\nThe election ended in a tie.")

# Function to determine the winner
def determine_winner(tally):
    """Determine the winner based on vote counts."""
    if tally["Candidate_A"] > tally["Candidate_B"]:
        return "Candidate_A"
    elif tally["Candidate_B"] > tally["Candidate_A"]:
        return "Candidate_B"
    else:
        return None  # Tie situation

# Function to run the entire voting system
def run_voting_system():
    """Main function to run the electronic voting system."""
    votes_db = {}
    print("Welcome to the Electronic Voting System!")
    
    while True:
        try:
            voter_count = int(input("Enter the number of voters: "))
            if voter_count <= 0:
                raise ValueError("The number of voters must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")
    
    for i in range(voter_count):
        voter_id = generate_voter_id()
        print(f"\nVoter {i + 1} ID: {voter_id}")
        cast_vote(voter_id, votes_db)
    
    tally_votes(votes_db)

# Function to start the voting system
def main():
    """Entry point for the voting system."""
    run_voting_system()

# Run the voting system
if __name__ == "_main_":
    main()