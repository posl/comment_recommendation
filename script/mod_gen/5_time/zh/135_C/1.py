def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        if A[i] > B[i]:
            A[i] -= B[i]
            ans += min(A[i + 1], A[i])
            A[i + 1] -= A[i]
    print(ans)

if __name__ == '__main__':
    main()