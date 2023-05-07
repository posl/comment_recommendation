def main():
    #input
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    #solve
    for i in range(N):
        if A[i] > X:
            A[i] = X
    #output
    print(sum(A))
