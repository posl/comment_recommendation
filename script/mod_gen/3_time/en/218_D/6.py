def solve():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x_count = {}
    y_count = {}
    for i in range(n):
        if x[i] in x_count:
            x_count[x[i]] += 1
        else:
            x_count[x[i]] = 1
        if y[i] in y_count:
            y_count[y[i]] += 1
        else:
            y_count[y[i]] = 1
    x_ans = 0
    y_ans = 0
    for i in x_count:
        x_ans += x_count[i] * (x_count[i] - 1) // 2
    for i in y_count:
        y_ans += y_count[i] * (y_count[i] - 1) // 2
    print(x_ans + y_ans)

if __name__ == '__main__':
    solve()