def get_median(list):
    list.sort()
    return list[4]
N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
ans = 10**9
for i in range(N-K+1):
    for j in range(N-K+1):
        list = []
        for k in range(K):
            for l in range(K):
                list.append(A[i+k][j+l])
        ans = min(ans, get_median(list))
print(ans)
