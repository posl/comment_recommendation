def solve():
    W = int(input())
    if W <= 2:
        print(1)
        print(W)
        return
    if W <= 4:
        print(2)
        print(1, W - 1)
        return
    if W <= 6:
        print(3)
        print(1, 2, W - 3)
        return
    print(4)
    print(1, 2, 3, W - 6)
    return
