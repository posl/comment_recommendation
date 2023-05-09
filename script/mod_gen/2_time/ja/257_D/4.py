def main():
    n = int(input())
    x, y, p = [], [], []
    for i in range(n):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ans = max(ans, (abs(x[i] - x[j]) + abs(y[i] - y[j])) // p[i])
    print(ans + 1)

if __name__ == '__main__':
    main()