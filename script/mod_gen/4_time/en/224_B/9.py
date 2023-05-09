def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    return "Yes" if all(A[i][j] + A[i+1][j+1] <= A[i+1][j] + A[i][j+1] for i in range(H-1) for j in range(W-1)) else "No"
print(solve())

if __name__ == '__main__':
    solve()