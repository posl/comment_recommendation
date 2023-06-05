def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(Q):
        x,k = map(int,input().split())
        print(A.index(x,k-1)+1 if x in A[k-1:] else -1)
