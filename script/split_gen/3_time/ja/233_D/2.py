def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    d = {0: 1}
    for a in A:
        s += a
        ans += d.get(s - K, 0)
        d[s] = d.get(s, 0) + 1
    print(ans)
