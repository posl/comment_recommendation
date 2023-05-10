def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        key = ''.join(sorted(s[i]))
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()