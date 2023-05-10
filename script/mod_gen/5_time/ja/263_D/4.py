def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] < L:
            A[i] = L
        elif A[i] > R:
            A[i] = R
    print(sum(A))

if __name__ == '__main__':
    main()