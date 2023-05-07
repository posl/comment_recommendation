def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        if N - A[i] < 0:
            print(N)
            exit()
        else:
            N -= A[i]
    print(-1)
