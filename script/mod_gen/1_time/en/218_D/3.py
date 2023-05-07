def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x = sorted(x)
    y = sorted(y)
    xcount = [0] * (10 ** 9 + 1)
    ycount = [0] * (10 ** 9 + 1)
    for i in range(n):
        xcount[x[i]] += 1
        ycount[y[i]] += 1
    xsum = [0] * (10 ** 9 + 1)
    ysum = [0] * (10 ** 9 + 1)
    for i in range(1, 10 ** 9 + 1):
        xsum[i] = xsum[i - 1] + xcount[i]
        ysum[i] = ysum[i - 1] + ycount[i]
    ans = 0
    for i in range(n):
        ans += (xsum[x[i] - 1]) * (n - xsum[x[i]])
        ans += (ysum[y[i] - 1]) * (n - ysum[y[i]])
    print(ans // 2)

if __name__ == '__main__':
    main()