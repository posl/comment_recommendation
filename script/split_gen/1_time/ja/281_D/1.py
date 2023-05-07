def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        for j in range(i+1,K):
            S.add(A[i]+A[j])
    ans = -1
    for x in S:
        if x%D==0:
            ans = max(ans,x)
    print(ans)
