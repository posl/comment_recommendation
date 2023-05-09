def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if A[i]*P + A[j]*Q + A[k]*R == 0:
                    ans = "Yes"
                    break
    print(ans)
