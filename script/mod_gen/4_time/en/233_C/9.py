def main():
    import sys
    from collections import defaultdict
    readline = sys.stdin.readline
    N, X = map(int, readline().split())
    D = defaultdict(list)
    for _ in range(N):
        *A, = map(int, readline().split())
        for a in A[1:]:
            D[a].append(A[0])
    ans = 0
    for a, L in D.items():
        if X % a != 0:
            continue
        b = X // a
        if b in D:
            if b == a:
                ans += len(L) * (len(L) - 1) // 2
            else:
                ans += len(L) * len(D[b])
    print(ans)

if __name__ == '__main__':
    main()