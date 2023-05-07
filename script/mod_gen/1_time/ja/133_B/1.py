def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            sum = 0
            for k in range(D):
                sum += (X[i][k] - X[j][k]) ** 2
            if int(sum ** 0.5) == sum ** 0.5:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()