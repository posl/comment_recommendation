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
            if (y[i] - y[j]) / (x[i] - x[j]) >= -1 and (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()