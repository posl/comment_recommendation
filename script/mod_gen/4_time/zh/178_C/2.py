def main():
    n = int(input())
    mod = 10**9 + 7
    print((pow(10,n,mod) - pow(9,n,mod) - pow(9,n,mod) + pow(8,n,mod))%mod)

if __name__ == '__main__':
    main()