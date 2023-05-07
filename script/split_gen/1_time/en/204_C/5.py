def main():
    N,M = map(int,input().split())
    A=[]
    B=[]
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    if M==0:
        print(N*N)
        return
    if M==N*(N-1)//2:
        print(0)
        return
    A = set(A)
    B = set(B)
    A = list(A)
    B = list(B)
    A.sort()
    B.sort()
    A = [0]+A
    B = [0]+B
    A.append(N+1)
    B.append(N+1)
    ans = 0
    for i in range(len(A)-1):
        for j in range(len(B)-1):
            if A[i+1]-A[i]==1 and B[j+1]-B[j]==1:
                continue
            else:
                ans += (A[i+1]-A[i])*(B[j+1]-B[j])
    print(ans)
