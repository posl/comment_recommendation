def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, list(input()))))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i < N//2:
                if j < N//2:
                    ans += max(A[i][j], A[i][N-1-j], A[N-1-i][j], A[N-1-i][N-1-j])
                else:
                    ans += max(A[i][j], A[N-1-i][j])
            else:
                if j < N//2:
                    ans += max(A[i][j], A[i][N-1-j])
                else:
                    ans += A[i][j]
    print(ans)
