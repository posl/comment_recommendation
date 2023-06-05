def main():
    n = int(input())
    ans = 0
    while n > 1:
        ans += 1
        #print("n=", n)
        max = 0
        maxp = 0
        for p in range(2, int(n**0.5)+1):
            if n % p == 0:
                #print("p=", p)
                e = 0
                tmp = n
                while tmp % p == 0:
                    tmp = tmp // p
                    e += 1
                if e > max:
                    max = e
                    maxp = p
        if max == 0:
            break
        #print("maxp=", maxp)
        n = n // maxp
    print(ans)

if __name__ == '__main__':
    main()