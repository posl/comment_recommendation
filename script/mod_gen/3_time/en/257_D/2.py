def main():
    N = int(input())
    x = []
    y = []
    p = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    ans = 0
    for i in range(N):
        for j in range(N):
            if p[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                ans = (abs(x[i] - x[j]) + abs(y[i] - y[j])) // p[i]
    print(ans)
main()

if __name__ == '__main__':
    main()