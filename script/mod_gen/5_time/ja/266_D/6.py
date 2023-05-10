def main():
    n = int(input())
    data = []
    for i in range(n):
        t,x,a = map(int,input().split())
        data.append([t,x,a])
    data = sorted(data)
    ans = 0
    for i in range(n):
        t,x,a = data[i]
        if x == 0:
            ans += a
        else:
            for j in range(i):
                t0,x0,a0 = data[j]
                if t0 + abs(x0-x) <= t:
                    ans += a
                    break
    print(ans)

if __name__ == '__main__':
    main()