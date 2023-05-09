def main():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            ans += 1
    print(ans)
