def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = 0
    r = N - 1
    ans = 0
    while l <= r:
        if A[l] + A[r] >= K:
            ans += 1
            r -= 1
        l += 1
    print(ans)

if __name__ == '__main__':
    main()