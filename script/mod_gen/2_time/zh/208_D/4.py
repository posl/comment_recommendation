def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    k = K
    for i in range(N):
        if k >= N:
            A[i] += k // N
        else:
            A[i] += 0
        k = k - 1
    for i in range(N):
        print(A[i])

if __name__ == '__main__':
    main()