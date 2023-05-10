def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for a in A:
        idx = bisect.bisect_left(B, a)
        if idx < M:
            ans = min(ans, abs(a - B[idx]))
        if idx > 0:
            ans = min(ans, abs(a - B[idx - 1]))
    print(ans)

if __name__ == '__main__':
    main()