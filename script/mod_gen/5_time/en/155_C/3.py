def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S_count = {}
    for s in S:
        if s not in S_count:
            S_count[s] = 1
        else:
            S_count[s] += 1
    max_count = max(S_count.values())
    for k, v in S_count.items():
        if v == max_count:
            print(k)

if __name__ == '__main__':
    main()