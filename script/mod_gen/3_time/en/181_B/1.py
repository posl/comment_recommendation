def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (B[i] + A[i]) // 2
    print(ans % 998244353)

if __name__ == '__main__':
    main()