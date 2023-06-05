def solve(n):
    if n <= 3:
        print(1)
        print(n)
        return
    elif n == 4:
        print(2)
        print(1, 2)
        return
    elif n == 5:
        print(2)
        print(2, 3)
        return
    elif n == 6:
        print(3)
        print(1, 2, 3)
        return
    else:
        print(3)
        print(1, 2, 4)
        return

if __name__ == '__main__':
    solve()