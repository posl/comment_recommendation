def solve(x,y):
    if (x+y)%3!=0:
        return 0
    n=(x+y)//3
    m=x-n
    if m<0:
        return 0
    return combination(n,m)

if __name__ == '__main__':
    solve()