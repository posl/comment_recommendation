def solve():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] < A[j]:
                result[i] += 1
    for i in range(N):
        print(result[i])
solve()
