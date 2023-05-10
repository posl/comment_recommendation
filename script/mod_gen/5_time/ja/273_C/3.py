def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    K = [0] * N
    for i in range(N):
        K[i] = A.count(A[i])
    total = sum(K)
    for i in range(N):
        if i == 0:
            print(total - K[i])
        else:
            print(total - K[i] - sum(K[:i]))

if __name__ == '__main__':
    main()