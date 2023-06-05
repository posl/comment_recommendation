def main():
    s = input()
    n = len(s)
    m = [0] * 2019
    m[0] = 1
    t = 0
    d = 1
    for i in range(n):
        t = (t + int(s[n - i - 1]) * d) % 2019
        m[t] += 1
        d = (d * 10) % 2019
    ans = 0
    for i in range(2019):
        ans += m[i] * (m[i] - 1) // 2
    print(ans)
