def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = {0: 1}
    s = 0
    ans = 0
    for i in range(N):
        s += A[i]
        ans += d.get(s - K, 0)
        d[s] = d.get(s, 0) + 1
    print(ans)
