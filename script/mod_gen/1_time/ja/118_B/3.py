def main():
    N, M = map(int, input().split())
    food = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for j in range(K):
            food[A[j]-1] += 1
    print(food.count(N))

if __name__ == '__main__':
    main()