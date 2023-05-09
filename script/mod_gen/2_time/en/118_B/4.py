def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for j in range(K):
            foods[A[j] - 1] += 1
    print(foods.count(N))

if __name__ == '__main__':
    main()