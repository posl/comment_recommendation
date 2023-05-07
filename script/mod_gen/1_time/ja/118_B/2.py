def main():
    N, M = map(int, input().split())
    food = [0] * M
    for _ in range(N):
        K, *A = map(int, input().split())
        for a in A:
            food[a-1] += 1
    print(food.count(N))

if __name__ == '__main__':
    main()