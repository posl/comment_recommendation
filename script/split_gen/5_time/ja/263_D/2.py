def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] > A[i+1]:
            ans += (A[i]-A[i+1])*L
        elif A[i] < A[i+1]:
            ans += (A[i+1]-A[i])*R
    print(ans)
