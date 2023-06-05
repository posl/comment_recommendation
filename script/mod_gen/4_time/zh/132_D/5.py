def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = [0] * k
    for i in range(1, k+1):
        ans[i-1] = (pow(k, i, mod) - pow(k-1, i, mod)) * pow(k, n-i, mod) % mod
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()