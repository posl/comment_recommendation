def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(M):
            B[i][j] -= i*7 + j + 1
    for i in range(N):
        for j in range(M):
            if B[i][j] < 0:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()