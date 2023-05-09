def main():
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    A.sort()
    A = [list(x) for x in zip(*A)]
    A.sort()
    A = [list(x) for x in zip(*A)]
    min_height = 10**9
    for i in range(N-K+1):
        for j in range(N-K+1):
            height = A[i+K-1][j+K-1]
            if K % 2 == 0:
                height += A[i+K-1][j+K-2]
                height += A[i+K-2][j+K-1]
                height += A[i+K-2][j+K-2]
                height //= 4
            else:
                height += A[i+K-1][j+K-2]
                height += A[i+K-2][j+K-1]
                height += A[i+K-2][j+K-2]
                height //= 4
                height += A[i+K-1][j+K-2]
                height += A[i+K-2][j+K-1]
                height += A[i+K-2][j+K-2]
                height //= 4
                height += A[i+K-1][j+K-2]
                height += A[i+K-2][j+K-1]
                height += A[i+K-2][j+K-2]
                height //= 4
            if height < min_height:
                min_height = height
    print(min_height)
