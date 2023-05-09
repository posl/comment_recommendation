def solve():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if min(A[i], A[j]) == i+1 and max(A[i], A[j]) == j+1:
                result += 1
    print(result)
