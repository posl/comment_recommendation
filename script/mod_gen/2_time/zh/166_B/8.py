def main():
    n,k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    flag = [0 for i in range(n)]
    for i in range(k):
        for j in range(d[i]):
            flag[a[i][j]-1] += 1
    ans = 0
    for i in range(n):
        if flag[i] == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()