def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(1, 200001):
        water[i] += water[i - 1]
        if water[i] > W:
            print("No")
            return
    print("Yes")
