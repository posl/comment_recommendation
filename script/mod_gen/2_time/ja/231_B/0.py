def main():
    n = int(input())
    candidates = {}
    for i in range(n):
        s = input()
        if s in candidates:
            candidates[s] += 1
        else:
            candidates[s] = 1
    max_vote = max(candidates.values())
    for name, vote in candidates.items():
        if vote == max_vote:
            print(name)
            break

if __name__ == '__main__':
    main()