def main():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] -= i*7+j+1
    for i in range(N):
        for j in range(M):
            if B[i][j] < 0:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()