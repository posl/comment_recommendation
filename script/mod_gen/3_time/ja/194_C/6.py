def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    ans = 0
    for i in range(N):
        ans += (N-i-1)*A[i]**2 - 2*A[i]*(B[N]-B[i+1]) + (B[N]-B[i+1])**2
    print(ans)

if __name__ == '__main__':
    main()