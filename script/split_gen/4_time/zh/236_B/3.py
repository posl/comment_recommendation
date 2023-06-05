def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    for i in range(0, 4*N, 2):
        if A[i] != A[i+1]:
            print(A[i])
            break
solve()
