def main():
    from collections import defaultdict
    from math import sqrt
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    L = [a[0] for a in A]
    B = [a[1:] for a in A]
    d = defaultdict(int)
    for i in range(N):
        for j in range(L[i]):
            d[B[i][j]] += 1
    ans = 0
    for i in range(N):
        for j in range(L[i]):
            if X % B[i][j] == 0:
                if X // B[i][j] in d:
                    ans += d[X // B[i][j]]
                if X // B[i][j] == B[i][j]:
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    main()