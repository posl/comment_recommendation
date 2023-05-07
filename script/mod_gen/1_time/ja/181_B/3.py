def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (A[i] + B[i]) * (B[i] - A[i] + 1) // 2
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()