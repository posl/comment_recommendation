def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i] < 0:
            A[i] = -1*A[i]
    if L > R:
        A.sort(reverse=True)
        A[L-1:N] = [R]*(N-L+1)
    else:
        A.sort()
        A[0:L] = [L]*(L)
    print(sum(A))
