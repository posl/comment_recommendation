def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(1,N+1):
        ans += (2**(N-i) - 2**(N-i-1)) * i * A[i-1]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()