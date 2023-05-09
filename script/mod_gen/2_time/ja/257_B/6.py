def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(Q):
        if A[L[i]-1] < N:
            if A[L[i]] != A[L[i]-1] + 1:
                A[L[i]] += 1
                A[L[i]-1] += 1
    for i in range(K):
        print(A[i], end=" ")
    print()

if __name__ == '__main__':
    main()