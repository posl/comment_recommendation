def solve(N, A, B):
    res = 0
    for x in range(1, 1001):
        for i in range(N):
            if x < A[i] or x > B[i]:
                break
        else:
            res += 1
    return res
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))
