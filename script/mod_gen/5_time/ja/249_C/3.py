def main():
    n,k = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1<<n):
        t = []
        for j in range(n):
            if i & 1<<j:
                t.append(s[j])
        if len(t) == k:
            x = set("".join(t))
            if len(x) > ans:
                ans = len(x)
    print(ans)

if __name__ == '__main__':
    main()