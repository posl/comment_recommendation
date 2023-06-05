def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    for i in range(N-K):
        if A[i] > A[i+K]:
            print("Yes")
            return
    print("No")
