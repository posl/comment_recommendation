def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += pow(2, i, 998244353) * (N - i) * A[i]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()