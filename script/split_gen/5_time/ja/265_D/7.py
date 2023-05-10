def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    res = 10**100
    for i in range(N-3+1):
        for j in range(i+1,N-2+1):
            for k in range(j+1,N-1+1):
                for l in range(k+1,N+1):
                    tmp = abs(P-A[i]*(j-i)+Q-A[j]*(k-j)+R-A[k]*(l-k))
                    if tmp < res:
                        res = tmp
    print(res)
