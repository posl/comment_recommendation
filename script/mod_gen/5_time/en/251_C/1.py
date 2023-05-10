def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in d:
            d[s] = max(d[s], t)
        else:
            d[s] = t
    ans = sorted(d.items(), key=lambda x: x[1], reverse=True)[0]
    print(ans[0])

if __name__ == '__main__':
    main()