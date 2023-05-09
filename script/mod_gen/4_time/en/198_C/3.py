def solve():
    R,X,Y = map(int,input().split())
    if (X**2+Y**2)**0.5 == R:
        print(1)
    elif (X**2+Y**2)**0.5 < R:
        print(2)
    else:
        print(int((X**2+Y**2)**0.5//R)+1)

if __name__ == '__main__':
    solve()