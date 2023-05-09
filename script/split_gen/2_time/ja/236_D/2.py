def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = []
    for i in range(N):
        for j in range(i+1, N):
            B.append(A[i][j-i-1])
    print(solve(N, B))
