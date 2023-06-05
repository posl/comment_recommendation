def main():
    n = int(input())
    print(1)
    a = int(input())
    if a == 0:
        exit()
    if a == 2*n+1:
        print(2*n+1)
        exit()
    if a == 2:
        print(3)
        exit()
    l = 2
    r = 2*n
    while 1:
        m = (l+r)//2
        print(m)
        b = int(input())
        if b == 0:
            exit()
        if b == a:
            if (m-l)%2 == 0:
                r = m-1
            else:
                l = m+1
        else:
            if (m-l)%2 == 0:
                l = m+1
            else:
                r = m-1
main()
