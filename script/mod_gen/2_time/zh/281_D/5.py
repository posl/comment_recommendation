def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    T = T % sumA
    for i in range(N):
        if A[i] > T:
            print(i+1, T)
            break
        T -= A[i]
solve()
