def buy_apple(x,y,n):
    if x > y:
        return y*n
    else:
        if n%3 == 0:
            return x*n/3
        else:
            return (n/3)*x + (n%3)*y
