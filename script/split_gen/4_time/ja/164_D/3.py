def main():
    s = input()
    n = len(s)
    t = [0] * n
    t[n-1] = int(s[n-1])
    for i in range(n-2, -1, -1):
        t[i] = (t[i+1] + int(s[i]) * pow(10, n-i-1, 2019)) % 2019
    t.sort()
    ans = 0
    cnt = 0
    for i in range(n):
        if t[i] == 0:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    ans += cnt * (cnt + 1) // 2
    print(ans)
