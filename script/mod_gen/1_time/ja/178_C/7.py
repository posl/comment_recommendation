def main():
    n = int(input())
    ans = 0
    mod = 10**9+7
    for i in range(1,n+1):
        ans = (ans + (pow(10,i,mod)-pow(9,i,mod)-pow(9,i,mod)+pow(8,i,mod))%mod)%mod
    print(ans)

if __name__ == '__main__':
    main()