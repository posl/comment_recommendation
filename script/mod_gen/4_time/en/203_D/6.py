def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
    else:
        return arr[len(arr)//2]
N, K = map(int, input().split())
A = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    a = list(map(int, input().split()))
    for j in range(1, N+1):
        A[i][j] = A[i-1][j] + A[i][j-1] - A[i-1][j-1] + a[j-1]
ans = float('inf')
for i in range(1, N-K+2):
    for j in range(1, N-K+2):
        arr = []
        for k in range(K):
            for l in range(K):
                arr.append(A[i+k][j+l] - A[i+k][j-1] - A[i-1][j+l] + A[i-1][j-1])
        ans = min(ans, median(arr))
print(int(ans))

if __name__ == '__main__':
    median()