def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #P+Q+Rの最大値を求める
    max_pqr = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                max_pqr = max(max_pqr, P*A[i]+Q*A[j]+R*A[k])
    #P+Q+Rの最大値を満たす(x,y,z,w)を求める
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if P*A[i]+Q*A[j]+R*A[k] == max_pqr:
                    print("Yes")
                    return
    print("No")
