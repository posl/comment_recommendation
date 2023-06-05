def buy_apple(x,y,n):
    if n%3 == 0:
        return min(n/3*y,n/3*2*x)
    elif n%3 == 1:
        return min((n-1)/3*y + x,(n-1)/3*2*x + y)
    else:
        return min((n-2)/3*y + 2*x,(n-2)/3*2*x + 2*y)
