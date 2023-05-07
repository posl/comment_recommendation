def main():
    n = int(input())
    votes = [input() for _ in range(n)]
    vote_count = {}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    max_count = max(vote_count.values())
    for k, v in sorted(vote_count.items(), key=lambda x: x[0]):
        if v == max_count:
            print(k)

if __name__ == '__main__':
    main()