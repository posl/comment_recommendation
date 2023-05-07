def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(Q):
        if L[i] == 1:
            if A[0] == N:
                pass
            elif A[1] != A[0] + 1:
                A[0] += 1
        elif L[i] == K:
            if A[K-1] == N:
                pass
            elif A[K-1] != A[K-2] + 1:
                A[K-1] += 1
        else:
            if A[L[i]-1] == N:
                pass
            elif A[L[i]] != A[L[i]-1] + 1:
                A[L[i]-1] += 1
    for i in A:
        print(i, end=' ')

if __name__ == '__main__':
    main()