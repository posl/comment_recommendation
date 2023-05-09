def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        while True:
            while r < N and A[r] >= x:
                r += 1
            if r == N:
                break
            if l == r:
                l += 1
                r += 1
            else:
                ans = max(ans, x*(r-l))
                l += 1
    print(ans)
