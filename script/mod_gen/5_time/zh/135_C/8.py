def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    # B = list(map(int, input().split()))
    N = 2
    A = [3, 5, 2]
    B = [4, 5]
    # N = 3
    # A = [5, 6, 3, 8]
    # B = [5, 100, 8]
    # N = 2
    # A = [100, 1, 1]
    # B = [1, 100]
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i + 1] <= B[i]:
            ans += A[i + 1]
            B[i] -= A[i + 1]
            A[i + 1] = 0
        else:
            ans += B[i]
            A[i + 1] -= B[i]
            B[i] = 0
    print(ans)

if __name__ == '__main__':
    main()