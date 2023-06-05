def solve():
    n,a,b=input().split()
    s=input()
    n=int(n)
    a=int(a)
    b=int(b)
    #print(n,a,b,s)
    if n%2==0:
        #print("n为偶数")
        if a>b:
            #print("a>b")
            #print("b*(n//2)+a")
            print(b*(n//2)+a)
        else:
            #print("a<=b")
            #print("a*n")
            print(a*n)
    else:
        #print("n为奇数")
        if a>b:
            #print("a>b")
            #print("b*(n//2)+a")
            print(b*(n//2)+a)
        else:
            #print("a<=b")
            #print("a*(n-1)+b")
            print(a*(n-1)+b)
