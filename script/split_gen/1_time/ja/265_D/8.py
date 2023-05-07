def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,P,Q,R)
    #print(A)
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    if A[i]+A[j]+A[k]+A[l] == P+Q+R:
                        ans = "Yes"
                        break
    print(ans)
