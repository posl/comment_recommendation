def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    C = [0] * N
    for i in range(N):
        C[i] = B[i] - A[i] + 1
    ans = 1
    for i in range(N):
        ans *= C[i]
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()