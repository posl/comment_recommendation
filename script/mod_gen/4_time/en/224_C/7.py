def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (y[i] - y[j]) * (x[i] - x[k]) != (y[i] - y[k]) * (x[i] - x[j]):
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()