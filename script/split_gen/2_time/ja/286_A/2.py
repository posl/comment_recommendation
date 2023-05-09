def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[P-1:Q] + A[R-1:S]
    A[P-1:Q] = A[R-1:S]
    A[R-1:S] = B
    for i in range(N):
        print(A[i],end=" ")
    print()
