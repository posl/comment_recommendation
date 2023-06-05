def main():
    N = int(input())
    x = []
    y = []
    P = []
    for _ in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if P[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()