def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    s = 0
    l = 0
    r = 0
    while l < N:
        while r < N and s + A[r] < K:
            s += A[r]
            r += 1
        ans += r - l
        s -= A[l]
        l += 1
        if l == r:
            r += 1
    print(ans)
