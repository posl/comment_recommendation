def main():
    n, k = map(int, input().split())
    mod = 1000000007
    for i in range(1, k+1):
        print(((k-i+1)*pow(k, mod-2, mod)*pow(k-1, i-1, mod))%mod)

if __name__ == '__main__':
    main()