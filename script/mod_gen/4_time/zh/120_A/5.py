def solve():
    a,b,c = map(int,input().split())
    if b >= a*c:
        print(c)
    else:
        print(b//a)

if __name__ == '__main__':
    solve()