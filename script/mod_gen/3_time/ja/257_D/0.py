def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    p = [0] * N
    for i in range(N):
        x[i], y[i], p[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans = max(ans, (abs(x[i] - x[j]) + abs(y[i] - y[j]) - 1) // p[i] + 1)
    print(ans)

if __name__ == '__main__':
    main()