def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i - 1] + A[i]
    B.sort()
    ans = 0
    for i in range(N):
        ans += abs(B[i])
    print(ans)

if __name__ == '__main__':
    main()