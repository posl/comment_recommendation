def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        cnt = 0
        while l <= r and r < N:
            if A[l] >= x:
                cnt += 1
                l += 1
            elif A[r] >= x:
                cnt += 1
                r += 1
            else:
                l += 1
                r += 1
            ans = max(ans, cnt*x)
    print(ans)
