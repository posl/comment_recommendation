def solve(a,b):
    x = a / (a**2+b**2)**0.5
    y = b / (a**2+b**2)**0.5
    return x,y

if __name__ == '__main__':
    solve()