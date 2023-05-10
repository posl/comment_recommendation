def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] = min(A[i], R)
    for i in range(N-1):
        A[i+1] = min(A[i+1], A[i]+L)
    print(sum(A))

if __name__ == '__main__':
    main()