def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    left = 0
    right = sum(A)
    ans = 0
    for i in range(N):
        left += A[i]
        right -= A[i]
        ans += A[i] * (N - i - 1) - (right - left)
    print(ans)

if __name__ == '__main__':
    main()