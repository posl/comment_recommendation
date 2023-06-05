def solve(x,y,z):
    if x*z > 0:
        return abs(x-y)
    else:
        return abs(x+y)

if __name__ == '__main__':
    solve()