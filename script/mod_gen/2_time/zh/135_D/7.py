def fight_monsters(N, A, B):
    if N == 1:
        return min(A[0], B[0])
    else:
        res = 0
        for i in range(N):
            if A[i] <= B[i]:
                res += A[i]
                A[i] = 0
                B[i] -= A[i]
            else:
                res += B[i]
                A[i] -= B[i]
                B[i] = 0
            if A[i+1] <= B[i]:
                res += A[i+1]
                A[i+1] = 0
                B[i] -= A[i+1]
            else:
                res += B[i]
                A[i+1] -= B[i]
                B[i] = 0
        return res
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(fight_monsters(N, A, B))
