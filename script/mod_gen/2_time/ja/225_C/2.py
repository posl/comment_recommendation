def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        for j in range(M):
            if B[i][j] != (i+1) * 7 + j + 1:
                print("No")
                return
    print("Yes")
main()

if __name__ == '__main__':
    main()