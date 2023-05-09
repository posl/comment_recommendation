def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    for j in range(N):
        if j == N-1:
            print(A[j])
        else:
            print(A[j], end=' ')

if __name__ == '__main__':
    main()