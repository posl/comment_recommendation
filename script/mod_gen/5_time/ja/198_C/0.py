def solve():
    R, X, Y = map(int, input().split())
    if R ** 2 == X ** 2 + Y ** 2:
        print(1)
    elif R ** 2 > X ** 2 + Y ** 2:
        print(2)
    else:
        print(math.ceil((X ** 2 + Y ** 2) ** 0.5 / R))

if __name__ == '__main__':
    solve()