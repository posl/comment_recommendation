def main():
    s = input()
    n = len(s)
    s = s[::-1]
    ans = 0
    mod = 2019
    #print(s)
    #print(n)
    d = [0] * mod
    d[0] = 1
    now = 0
    for i in range(n):
        now += int(s[i]) * pow(10, i, mod)
        now %= mod
        ans += d[now]
        d[now] += 1
    print(ans)

if __name__ == '__main__':
    main()