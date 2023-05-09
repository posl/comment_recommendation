def solve(x,y,a,b):
    exp = 0
    while x*y > x+a and x*y < y+b:
        if x*a < x+b:
            x *= a
            exp += 1
        else:
            x += b
            exp += 1
    return exp
x,y,a,b = list(map(int,input().split()))
print(solve(x,y,a,b))

if __name__ == '__main__':
    solve()