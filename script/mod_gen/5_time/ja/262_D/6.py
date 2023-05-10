def main():
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    mod = 998244353
    ans = 0
    for a in A:
        ans += pow(2, N-1, mod) * a
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()