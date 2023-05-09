def main():
    import sys
    import bisect
    input = sys.stdin.readline
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        x = bisect.bisect_left(R, L[i] + D - 1)
        ans = max(ans, i - x + 1)
    print(ans)

if __name__ == '__main__':
    main()