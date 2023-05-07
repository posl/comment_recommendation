def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    for i in range(N):
        if i < K:
            A[i] = max(A[i] - X, 0)
    print(sum(A))

if __name__ == '__main__':
    main()