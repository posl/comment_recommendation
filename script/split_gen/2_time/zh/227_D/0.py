def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(N-1):
        B.append(A[i+1]-A[i])
    B.sort()
    ans = sum(B[:N-K])
    print(ans)
