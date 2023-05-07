def main():
    N, W = map(int, input().split())
    water = [0 for _ in range(200001)]
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(1, len(water)):
        water[i] += water[i-1]
    for w in water:
        if w > W:
            print("No")
            return
    print("Yes")
