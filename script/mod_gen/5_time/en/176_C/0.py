def main():
    N = int(input())
    A = list(map(int, input().split()))
    stools = [0] * N
    stools[0] = A[0]
    for i in range(1, N):
        stools[i] = max(stools[i-1], A[i])
    print(sum(stools) - sum(A))

if __name__ == '__main__':
    main()