def solve():
    x,y,z = map(int,input().split())
    if y > 0:
        print(-1)
        return
    print(-y+z)

if __name__ == '__main__':
    solve()