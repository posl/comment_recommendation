def main():
    N = int(input())
    S = [input() for _ in range(N)]
    from collections import Counter
    C = [Counter(s) for s in S]
    from collections import defaultdict
    D = defaultdict(int)
    for c in C:
        D[tuple(c.items())] += 1
    ans = 0
    for n in D.values():
        ans += n*(n-1)//2
    print(ans)

if __name__ == '__main__':
    main()