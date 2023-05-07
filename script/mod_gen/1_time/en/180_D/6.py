def solve():
    x,y,a,b = map(int,input().split())
    exp = 0
    while x < y and x * a < x + b:
        x *= a
        exp += 1
    exp += (y - x - 1) // b
    return exp
print(solve())

if __name__ == '__main__':
    solve()