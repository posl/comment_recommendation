def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        N = N - A[i]
        if N < 0:
            print(-1)
            return
    print(N)

if __name__ == '__main__':
    main()