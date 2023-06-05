def solve(x,y,z):
    if y>0 and y<z:
        return -1
    else:
        return abs(x-z)

if __name__ == '__main__':
    solve()