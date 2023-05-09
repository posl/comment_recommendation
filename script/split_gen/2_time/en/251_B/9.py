def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    w = A[0]
    if w == 1:
        print(W)
        return
    if w == 2:
        print((W + 1) // 2)
        return
    if w == 3:
        if W <= 2:
            print(0)
            return
        if W <= 4:
            print(1)
            return
        if W <= 6:
            print(2)
            return
        print(W - 5)
        return
    if w == 4:
        if W <= 3:
            print(0)
            return
        if W <= 6:
            print(1)
            return
        print(W - 5)
        return
    if w == 5:
        if W <= 4:
            print(0)
            return
        print(W - 4)
        return
    if w == 6:
        if W <= 5:
            print(0)
            return
        print(W - 5)
        return
    if w == 7:
        if W <= 6:
            print(0)
            return
        print(W - 6)
        return
    if w == 8:
        if W <= 7:
            print(0)
            return
        print(W - 7)
        return
    if w == 9:
        if W <= 8:
            print(0)
            return
        print(W - 8)
        return
    if w == 10:
        if W <= 9:
            print(0)
            return
        print(W - 9)
        return
    if w == 11:
        if W <= 10:
            print(0)
            return
        print(W - 10)
        return
    if w == 12:
        if W <= 11:
            print(0)
            return
        print(W - 11)
        return
    if w == 13:
        if W <= 12:
            print(0)
            return
        print(W - 12)
        return
    if w == 14:
        if W <= 13:
            print(0)
            return
        print(W - 13)
        return
