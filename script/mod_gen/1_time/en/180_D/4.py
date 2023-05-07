def solve(x,y,a,b):
    exp = 0
    str = x
    while str < y:
        if str * a < str + b:
            str = str * a
            exp += 1
        else:
            str += b
            exp += 1
    return exp

if __name__ == '__main__':
    solve()