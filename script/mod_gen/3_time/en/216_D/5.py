def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [0] * (N + 1)
    for i in range(M):
        B[A[i][0]] += 1
        B[A[i][1]] += 1
    for i in range(1, N + 1):
        if B[i] % 2 != 0:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()