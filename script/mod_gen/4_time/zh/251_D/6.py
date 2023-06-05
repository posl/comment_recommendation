def solve():
    W = int(input())
    if W <= 3:
        print(1)
        print(W)
    elif W <= 5:
        print(2)
        print(1, W - 1)
    elif W <= 8:
        print(3)
        print(1, W - 2, 1)
    elif W <= 11:
        print(4)
        print(1, W - 3, 2, 1)
    else:
        print(6)
        print(1, W - 5, 2, 2, 2, 1)

if __name__ == '__main__':
    solve()