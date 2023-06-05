def main():
    n,m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for i in range(n):
        for j in range(1, len(a[i])):
            b.append(a[i][j])
    c = [0 for i in range(m)]
    for i in range(len(b)):
        c[b[i]-1] += 1
    ans = 0
    for i in range(len(c)):
        if c[i] == n:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()