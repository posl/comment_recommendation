def solve():
    R, X, Y = map(int, input().split())
    dist = (X**2 + Y**2)**0.5
    if dist < R:
        print(2)
    else:
        print(int(dist//R + (dist%R != 0)))

if __name__ == '__main__':
    solve()