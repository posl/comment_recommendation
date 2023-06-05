def buy_apple(x,y,n):
    if n%3==0:
        return min(x*n/3,y*n/3)
    elif n%3==1:
        return min(x*(n-1)/3+y,y*(n-1)/3+x)
    else:
        return min(x*(n-2)/3+2*y,y*(n-2)/3+2*x)
