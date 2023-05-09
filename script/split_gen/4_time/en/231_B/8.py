def main():
    # Take input
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # Count votes
    votes = {}
    for i in range(n):
        if s[i] in votes:
            votes[s[i]] += 1
        else:
            votes[s[i]] = 1
    # Find winner
    winner = None
    max_vote = 0
    for key, value in votes.items():
        if value > max_vote:
            max_vote = value
            winner = key
    # Print winner
    print(winner)
