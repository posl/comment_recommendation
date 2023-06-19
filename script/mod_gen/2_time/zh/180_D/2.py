def solve(x,y,a,b):
    if x>=y:
        return 0
    if b>=a:
        return (y-x-1)//a
    else:
        if (x*b)%a==0:
            return max((y-x-1)//a,(y-x-1)//a*(x*b)//a)
        else:
            return max((y-x-1)//a,(y-x-1)//a*(x*b)//a,(y-x-1)//a*(x*b)//a+1)

if __name__ == '__main__':
    solve()