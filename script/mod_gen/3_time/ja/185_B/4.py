def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai-0.5)
        b.append(bi-0.5)
    #print(a)
    #print(b)
    for i in range(m):
        if i == 0:
            if a[i] > 0:
                print("No")
                exit()
            else:
                n -= a[i]
        else:
            if a[i] - b[i-1] > 0:
                print("No")
                exit()
            else:
                n -= a[i] - b[i-1]
        #print(n)
        if n <= 0:
            print("No")
            exit()
        else:
            n += 1
            if n >  n:
                n = n
    if t - b[m-1] > 0:
        n -= t - b[m-1]
    else:
        print("No")
        exit()
    if n <= 0:
        print("No")
        exit()
    else:
        print("Yes")
        exit()

if __name__ == '__main__':
    main()