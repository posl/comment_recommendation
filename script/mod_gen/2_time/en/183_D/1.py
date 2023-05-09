def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(200000):
        water[i + 1] += water[i]
    if max(water) > W:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()