def fun(n,m):
    if n==1:
        return 1
    else:
        i=2
        while i*i<=m:
            if m%i==0:
                return fun(n-1,i)+fun(n-1,m//i)
            i+=1
        return 1

if __name__ == '__main__':
    fun()