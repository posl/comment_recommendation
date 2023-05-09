def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x_num = []
    y_num = []
    x_num.append(1)
    y_num.append(1)
    for i in range(N-1):
        if x[i] == x[i+1]:
            x_num[-1] += 1
        elif x[i] != x[i+1]:
            x_num.append(1)
        if y[i] == y[i+1]:
            y_num[-1] += 1
        elif y[i] != y[i+1]:
            y_num.append(1)
    x_num.sort(reverse=True)
    y_num.sort(reverse=True)
    x_ans = 0
    y_ans = 0
    for i in range(len(x_num)):
        x_ans += x_num[i] * (i + 1)
    for i in range(len(y_num)):
        y_ans += y_num[i] * (i + 1)
    print(x_ans * y_ans)

if __name__ == '__main__':
    main()