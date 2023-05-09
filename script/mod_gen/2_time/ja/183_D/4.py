def main():
    N, W = map(int, input().split())
    water = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(2 * 10 ** 5):
        water[i + 1] += water[i]
    print("Yes" if max(water) <= W else "No")

if __name__ == '__main__':
    main()