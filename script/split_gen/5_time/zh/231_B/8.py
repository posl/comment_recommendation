def main():
    n = int(input())
    votes = {}
    for i in range(n):
        s = input()
        if s not in votes:
            votes[s] = 1
        else:
            votes[s] += 1
    print(max(votes, key=votes.get))
