def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                continue
            s = []
            for k in range(N):
                s.append(A[(i+k)%N][j])
            ans = max(ans, int("".join(map(str, s))))
            s = []
            for k in range(N):
                s.append(A[i][(j+k)%N])
            ans = max(ans, int("".join(map(str, s))))
            s = []
            for k in range(N):
                s.append(A[(i+k)%N][(j+k)%N])
            ans = max(ans, int("".join(map(str, s))))
            s = []
            for k in range(N):
                s.append(A[(i+k)%N][(j-k)%N])
            ans = max(ans, int("".join(map(str, s))))
    print(ans)

if __name__ == '__main__':
    main()