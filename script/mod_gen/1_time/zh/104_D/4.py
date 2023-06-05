def main():
    s = input()
    q = s.count("?")
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    mod = 10**9+7
    ans = 0
    for i in range(q+1):
        for j in range(q+1-i):
            k = q-i-j
            tmp = 1
            tmp *= pow(3,i,mod)
            tmp *= pow(3,j,mod)
            tmp *= pow(3,k,mod)
            tmp *= pow(2,a,mod)
            tmp *= pow(2,b,mod)
            tmp *= pow(2,c,mod)
            tmp %= mod
            ans += tmp
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()