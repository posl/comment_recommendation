def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        l = i
        r = i
        x = A[i]
        while l > 0 and A[l-1] >= x:
            l -= 1
        while r < N-1 and A[r+1] >= x:
            r += 1
        ans = max(ans, x*(r-l+1))
    print(ans)
