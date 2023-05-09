def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    for i in range(M):
        N -= A[i]
        if N <= 0:
            if N == 0:
                print(0)
            else:
                print(-1)
            return
    print(N)
