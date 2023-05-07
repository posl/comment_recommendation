def main():
    W = int(input())
    if W == 2:
        print(2)
        print(1, 1)
        return
    if W == 3:
        print(3)
        print(1, 1, 1)
        return
    if W % 2 == 0:
        print(W)
        for i in range(1, W + 1):
            print(i, end = " ")
        print()
        return
    else:
        print(W + 1)
        for i in range(1, W + 2):
            print(i, end = " ")
        print()
        return
