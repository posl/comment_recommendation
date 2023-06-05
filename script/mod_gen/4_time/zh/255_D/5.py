def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    for i in range(Q):
        total = 0
        for j in range(N):
            total += abs(A[j] - X[i])
        print(total)

if __name__ == '__main__':
    main()