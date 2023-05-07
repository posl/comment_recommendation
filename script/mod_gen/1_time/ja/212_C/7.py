def main():
    import sys
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    A.sort()
    B.sort()
    ans = 10**9
    a = 0
    b = 0
    while a < N and b < M:
        ans = min(ans, abs(A[a]-B[b]))
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
    print(ans)

if __name__ == '__main__':
    main()