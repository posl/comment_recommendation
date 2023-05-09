def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10 ** 5 + 1):
        l = 0
        r = 0
        while l < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, (r - l) * x)
            while l < N and A[l] < x:
                l += 1
            l += 1
    print(ans)
