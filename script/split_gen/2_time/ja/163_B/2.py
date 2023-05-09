def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(M - i)
            return
    print(-1)
