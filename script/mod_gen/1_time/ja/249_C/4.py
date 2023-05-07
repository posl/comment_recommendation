def main():
    import sys
    from itertools import combinations
    from collections import Counter
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = [input().rstrip() for _ in range(N)]
    L = []
    for s in S:
        L += list(s)
    C = Counter(L)
    L = [x for x in C if C[x] >= K]
    ans = 0
    for i in range(K, len(L)+1):
        for c in combinations(L, i):
            cnt = 0
            for s in S:
                for x in c:
                    if x in s:
                        cnt += 1
                        break
            if cnt == K:
                ans = i
    print(ans)

if __name__ == '__main__':
    main()