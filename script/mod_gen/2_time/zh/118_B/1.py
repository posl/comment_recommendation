def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    food = [0] * M
    for i in range(N):
        for j in range(1, A[i][0] + 1):
            food[A[i][j] - 1] += 1
    print(food.count(N))

if __name__ == '__main__':
    main()