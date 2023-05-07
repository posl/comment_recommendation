def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        p.append(tmp[1])
        x.append(tmp[2])
    ans = 9999999999999999999
    for i in range(n):
        if x[i] > 0:
            ans = min(ans, p[i])
    if ans == 9999999999999999999:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()