def main():
    H, W, C = map(int, input().split())
    A = []
    for _ in range(H):
        A.extend(list(map(int, input().split())))
    min_cost = 10 ** 18
    for i in range(H * W):
        for j in range(i + 1, H * W):
            cost = A[i] + A[j] + C * (abs(i // W - j // W) + abs(i % W - j % W))
            if cost < min_cost:
                min_cost = cost
    print(min_cost)

if __name__ == '__main__':
    main()