def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    d = 0
    for i in range(N):
        d += abs(A[i]-B[i])
    if d <= K and (K-d)%2 == 0:
        print("Yes")
    else:
        print("No")
