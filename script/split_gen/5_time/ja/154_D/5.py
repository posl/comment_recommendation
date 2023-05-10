def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    psum = [0] * (n+1)
    for i in range(n):
        psum[i+1] = psum[i] + p[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, (psum[i+k] - psum[i] + k) / 2)
    print(ans)
