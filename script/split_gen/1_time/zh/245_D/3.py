def solve():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(m+1)
    for i in range(n+1):
        B[m] += C[n+m-i]*A[i]
    for i in range(m+1):
        B[i] = (C[i]-B[m])//A[0]
    print(' '.join(map(str,B)))
