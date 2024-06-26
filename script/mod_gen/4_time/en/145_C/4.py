def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    perm = [i for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
    ans *= (N - 1) / (N * math.factorial(N - 1))
    print(ans)

if __name__ == '__main__':
    main()