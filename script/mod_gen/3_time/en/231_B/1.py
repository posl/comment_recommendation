def main():
    N = int(input())
    votes = {}
    for i in range(N):
        name = input()
        if name in votes:
            votes[name] += 1
        else:
            votes[name] = 1
    max_votes = max(votes.values())
    for name, num_votes in votes.items():
        if num_votes == max_votes:
            print(name)
            break

if __name__ == '__main__':
    main()