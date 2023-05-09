def solve():
    x,y = map(int, input().split())
    print(y-x if y>x else 0)
solve()

if __name__ == '__main__':
    solve()