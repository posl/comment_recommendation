def main():
    N = int(input())
    votes = {}
    for i in range(N):
        vote = input()
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    max_votes = max(votes.values())
    for k, v in sorted(votes.items()):
        if v == max_votes:
            print(k)
