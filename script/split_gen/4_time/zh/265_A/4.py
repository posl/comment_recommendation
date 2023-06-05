def buy_apple(x,y,n):
    if x==y:
        return x*n
    if x>y:
        return y*n
    if x<y:
        if n%3==0:
            return n//3*y
        else:
            return (n//3+1)*y
