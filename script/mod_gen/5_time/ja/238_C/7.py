def main():
    N = int(input())
    mod = 998244353
    ans = 0
    for i in range(1,19):
        if N >= 10**i:
            ans += 9*i*10**(i-1)
        else:
            ans += (N-10**(i-1)+1)*i
            break
    print(ans%mod)

if __name__ == '__main__':
    main()