def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = -float('inf')
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N - 1:
                if j == 0 or j == N - 1:
                    continue
            if j == 0 or j == N - 1:
                if i == 0 or i == N - 1:
                    continue
            temp = 0
            for k in range(N):
                temp += A[i][k] * (10 ** k)
            for k in range(N):
                temp += A[k][j] * (10 ** (N + k))
            ans = max(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()