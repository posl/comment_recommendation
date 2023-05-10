def median(A):
    n = len(A)
    if n % 2 == 0:
        return (A[n//2-1] + A[n//2]) // 2
    else:
        return A[n//2]
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = []
for i in range(N-K+1):
    for j in range(N-K+1):
        l = []
        for k in range(K):
            for l in range(K):
                l.append(A[i+k][j+l])
        l.sort()
        B.append(l)
B.sort(key=lambda x: median(x))
print(median(B[0]))

if __name__ == '__main__':
    median()