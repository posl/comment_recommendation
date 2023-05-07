def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    A = A[:K]
    #print(A)
    if D == 1:
        ans = A[-1]
    else:
        ans = -1
        for i in range(1,D):
            for j in range(len(A)):
                if A[j] % D == i:
                    ans = max(ans,A[j])
                    break
    print(ans)
