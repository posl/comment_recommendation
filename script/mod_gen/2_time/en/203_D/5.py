def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    A.sort()
    print(A[K-1][K-1])

if __name__ == '__main__':
    main()