def main():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    water = [0] * (10**6 + 1)
    for i in range(N):
        water[S[i]] += P[i]
        water[T[i]] -= P[i]
    for i in range(1, 10**6 + 1):
        water[i] += water[i - 1]
    for i in range(10**6 + 1):
        if water[i] > W:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()