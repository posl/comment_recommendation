def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] = max(0, B[i]-A[i])
        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1]-B[i])
    print(ans)

if __name__ == '__main__':
    main()