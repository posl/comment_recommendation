def solve():
    w = int(input())
    if w <= 3:
        print(1)
        print(w)
    elif w <= 5:
        print(2)
        print(2, w - 2)
    else:
        print(3)
        print(2, 3, w - 5)

if __name__ == '__main__':
    solve()