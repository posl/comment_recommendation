def main():
    n = int(input())
    votes = {}
    for _ in range(n):
        name = input()
        if name in votes.keys():
            votes[name] += 1
        else:
            votes[name] = 1
    winner = max(votes, key=votes.get)
    print(winner)
