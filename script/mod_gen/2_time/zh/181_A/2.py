def solve(x,y,a,b):
    if a == 1:
        return (y-x)//b
    else:
        n = 0
        while x*a <= x+b and x*a < y:
            n += 1
            x *= a
        return n + (y-x-1)//b

if __name__ == '__main__':
    solve()