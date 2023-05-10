def main():
    n,k,a = map(int,input().split())
    #print(n,k,a)
    #n,k,a = 3,3,2
    #n,k,a = 1,100,1
    #n,k,a = 3,14,2
    if k <= n:
        print(k)
    else:
        k = k - n
        a = a + k
        if a > n:
            a = a - n
        print(a)

if __name__ == '__main__':
    main()