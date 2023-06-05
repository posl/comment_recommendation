def main():
    n = int(input())
    candidates = {}
    for i in range(n):
        name = input()
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1
    max_vote = 0
    winner = ""
    for name, vote in candidates.items():
        if vote > max_vote:
            max_vote = vote
            winner = name
    print(winner)

if __name__ == '__main__':
    main()