def main():
    s = input()
    n = len(s)
    mod = 2019
    m = [0] * mod
    m[0] = 1
    t = 0
    a = 1
    for i in range(n - 1, -1, -1):
        t = (t + int(s[i]) * a) % mod
        a = a * 10 % mod
        m[t] += 1
    ans = 0
    for i in range(mod):
        ans += m[i] * (m[i] - 1) // 2
    print(ans)
