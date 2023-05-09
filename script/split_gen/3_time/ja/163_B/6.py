def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(i)
            exit()
    print(-1)
