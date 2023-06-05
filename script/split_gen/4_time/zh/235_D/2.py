def solve(a,n):
    #print("a:",a,"n:",n)
    if n%a!=0:
        return -1
    if n==a:
        return 1
    if n==1:
        return 0
    if n<a:
        return -1
    result=0
    while n>=a:
        if n%a==0:
            n=n//a
            result+=1
        else:
            if n%10==1:
                n=n//10
                result+=1
            else:
                return -1
    return result
