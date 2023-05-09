def main():
    n = int(input())
    votes = [input() for _ in range(n)]
    max_vote = max(votes, key=votes.count)
    print(max_vote)
