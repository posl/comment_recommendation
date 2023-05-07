def main():
    import sys
    from itertools import combinations
    input = sys.stdin.readline
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for comb in combinations(A, K):
        S.add(sum(comb))
    ans = -1
    for s in S:
        if s % D == 0:
            ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()