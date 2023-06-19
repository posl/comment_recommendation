def main():
    # N = 2
    # A = [3, 5, 2]
    # B = [4, 5]
    # N = 3
    # A = [5, 6, 3, 8]
    # B = [5, 100, 8]
    # N = 2
    # A = [100, 1, 1]
    # B = [1, 100]
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] = max(0, B[i] - A[i])
        ans += min(A[i + 1], B[i])
        A[i + 1] = max(0, A[i + 1] - B[i])
    print(ans)

if __name__ == '__main__':
    main()