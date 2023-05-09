def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    D = []
    for i in range(N):
        d = A[i + 1] - A[i]
        D.append(d)
    print(sum(D) - max(D))

if __name__ == '__main__':
    main()