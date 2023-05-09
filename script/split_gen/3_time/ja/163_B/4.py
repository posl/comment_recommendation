def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        if A[i] <= N:
            N -= A[i]
        else:
            print(N)
            return
    print(-1)
