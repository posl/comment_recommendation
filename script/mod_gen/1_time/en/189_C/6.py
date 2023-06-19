def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10 ** 5 + 1):
        l = 0
        for r in range(N):
            while l <= r and A[l] < x:
                l += 1
            if l <= r:
                ans = max(ans, (r - l + 1) * x)
    print(ans)
main()
