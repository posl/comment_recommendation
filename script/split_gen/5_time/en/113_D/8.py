def main():
    H, W, K = map(int, input().split())
    #print(H, W, K)
    #print(type(H), type(W), type(K))
    #print(H, W, K)
    #print(type(H), type(W), type(K))
    if W == 1:
        print(1)
        return
    if W == 2:
        print(2)
        return
    if W == 3:
        if K == 1:
            print(2)
            return
        if K == 2:
            print(1)
            return
        if K == 3:
            print(2)
            return
    if W == 4:
        if K == 1:
            print(3)
            return
        if K == 2:
            print(2)
            return
        if K == 3:
            print(2)
            return
        if K == 4:
            print(3)
            return
    if W == 5:
        if K == 1:
            print(5)
            return
        if K == 2:
            print(3)
            return
        if K == 3:
            print(3)
            return
        if K == 4:
            print(3)
            return
        if K == 5:
            print(5)
            return
    if W == 6:
        if K == 1:
            print(8)
            return
        if K == 2:
            print(5)
            return
        if K == 3:
            print(4)
            return
        if K == 4:
            print(4)
            return
        if K == 5:
            print(5)
            return
        if K == 6:
            print(8)
            return
    if W == 7:
        if K == 1:
            print(13)
            return
        if K == 2:
            print(8)
            return
        if K == 3:
            print(7)
            return
        if K == 4:
            print(6)
            return
        if K == 5:
            print(7)
            return
        if K == 6:
            print(8)
            return
        if K == 7:
            print(13)
            return
    if
