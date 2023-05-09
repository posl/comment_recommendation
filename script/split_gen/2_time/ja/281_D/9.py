def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(N,K,D)
    #print(A)
    ans = -1
    for i in range(N):
        for j in range(i+1,N):
            x = A[i] + A[j]
            if x % D == 0:
                ans = max(ans,x)
    print(ans)
