def main():
    N = int(input())
    d = {}
    for i in range(N):
        s = input()
        l = list(s)
        l.sort()
        s = "".join(l)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()