def buy_apples(x,y,n):
    if n % 3 == 0:
        return min(x*n, n/3*y)
    else:
        return min(x*n, (n/3+1)*y)
