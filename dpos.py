import random

# Stakeholders and their stakes (votes)
stakeholders = {
    'Alice': 50,
    'Bob': 30,
    'Charlie': 20,
    'Diana': 10,
    'Eve': 40
}

# Delegate candidates
candidates = ['Validator1', 'Validator2', 'Validator3']

# Each stakeholder votes for a candidate (can be random or weighted)
def vote(stakeholders, candidates):
    votes = {candidate: 0 for candidate in candidates}
    for voter, stake in stakeholders.items():
        chosen = random.choice(candidates)
        votes[chosen] += stake
    return votes

# Simulate voting
vote_result = vote(stakeholders, candidates)
print("🗳 Voting Result:", vote_result)

# Select top delegate (highest total stake votes)
selected_delegate = max(vote_result, key=vote_result.get)
print(f"✅ Block is validated by: {selected_delegate}")
