def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    for i in range(0,N-K):
        #print(A[i],A[i+K])
        if A[i] == A[i+K]:
            print("No")
            return
    print("Yes")
