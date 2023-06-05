def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(1<<n):
        x = []
        for j in range(n):
            if i&(1<<j):
                x.append(s[j])
        x.sort()
        x = ''.join(x)
        ok = True
        for j in range(m):
            if t[j] in x:
                ok = False
                break
        if ok:
            print(x)
            return
    print(-1)

if __name__ == '__main__':
    main()