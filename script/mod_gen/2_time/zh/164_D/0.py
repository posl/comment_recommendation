def main():
    s = input()
    n = len(s)
    mod = 2019
    count = [0] * mod
    count[0] = 1
    now = 0
    ten = 1
    for i in range(n-1, -1, -1):
        now = (now + int(s[i]) * ten) % mod
        ten = (ten * 10) % mod
        count[now] += 1
    ans = 0
    for i in range(mod):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()