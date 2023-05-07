def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a_i % m for a_i in a]
    s = [0]
    for i in range(n):
        s.append((s[-1] + a[i]) % m)
    d = {i: 0 for i in range(m)}
    for i in range(n+1):
        d[s[i]] += 1
    ans = 0
    for key, val in d.items():
        ans += val * (val - 1) // 2
    print(ans)
