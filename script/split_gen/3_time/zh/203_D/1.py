def get_median(arr):
    arr.sort()
    return arr[len(arr)//2]
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 10**9
for i in range(N-K+1):
    for j in range(N-K+1):
        arr = []
        for x in range(K):
            for y in range(K):
                arr.append(A[i+x][j+y])
        ans = min(ans, get_median(arr))
print(ans)
