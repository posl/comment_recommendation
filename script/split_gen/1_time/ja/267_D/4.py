def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            B = A[i:j+1]
            if len(B) == M:
                tmp = 0
                for k in range(M):
                    tmp += (k+1)*B[k]
                ans = max(ans, tmp)
    print(ans)
