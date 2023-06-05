def time_to_make(n,x,t):
    if n%x == 0:
        return n/x*t
    else:
        return (n/x+1)*t
