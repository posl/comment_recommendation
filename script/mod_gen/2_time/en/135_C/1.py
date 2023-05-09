def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        ans += min(A[i+1], B[i] - min(A[i], B[i]))
        A[i+1] = max(A[i+1] - B[i] + min(A[i], B[i]), 0)
    print(ans)

if __name__ == '__main__':
    main()