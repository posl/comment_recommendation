def min_time(N, A, B):
    min_time = 1000000000
    for i in range(N):
        for j in range(N):
            if i != j:
                min_time = min(min_time, max(A[i], B[j]))
            else:
                min_time = min(min_time, A[i] + B[j])
    return min_time
N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
print(min_time(N, A, B))
