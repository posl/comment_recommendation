def main():
    s = input()
    n = len(s)
    m = [0] * 2019
    m[0] = 1
    t = 0
    for i in range(n):
        t = (t + int(s[n - 1 - i]) * pow(10, i, 2019)) % 2019
        m[t] += 1
    ans = 0
    for i in m:
        ans += i * (i - 1) // 2
    print(ans)
