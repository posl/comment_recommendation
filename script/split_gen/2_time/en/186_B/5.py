def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    ans = 10**10
    for i in range(H):
        for j in range(W):
            tmp = 0
            for k in range(H):
                for l in range(W):
                    tmp += abs(i-k) + abs(j-l) + abs(A[i][j]-A[k][l])
            ans = min(ans,tmp)
    print(ans)
