def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    bonus = [0] * N
    for _ in range(M):
        X, Y = map(int, input().split())
        bonus[X - 1] = Y
    time = T
    for i in range(N - 1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        time += bonus[i]
    print("Yes")

if __name__ == '__main__':
    main()