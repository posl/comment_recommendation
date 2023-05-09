def check(mid):
    for i in range(N-K+1):
        for j in range(N-K+1):
            if A[i][j] <= mid <= A[i+K-1][j+K-1]:
                return True
    return False
N, K = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]
A.sort()
A = [[A[i][j] for j in range(N)] for i in range(N)]
A.sort(key=lambda x: x[0])
ok = 10**9 + 1
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
The first half of the code is the same as the previous one. The second half is to perform binary search on the answer. In the binary search, we can check if the median is ok or not by the following function.

if __name__ == '__main__':
    check()