def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    A = [[0 for _ in range(7)] for _ in range(10**2)]
    for i in range(10**2):
        for j in range(7):
            A[i][j] = i*7 + j + 1
    for i in range(N):
        for j in range(M):
            if B[i][j] != A[i][j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()