def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return
    print(N)

if __name__ == '__main__':
    main()