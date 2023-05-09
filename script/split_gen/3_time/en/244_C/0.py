def main():
    N = int(input())
    print(1)
    a = int(input())
    if a == 0:
        return
    print(2)
    b = int(input())
    if b == 0:
        return
    print(3)
    c = int(input())
    if c == 0:
        return
    if a == 2:
        if b == 1:
            if c == 3:
                print(4)
            else:
                print(3)
        else:
            if c == 3:
                print(5)
            else:
                print(2)
    else:
        if b == 1:
            if c == 3:
                print(5)
            else:
                print(2)
        else:
            if c == 3:
                print(4)
            else:
                print(1)
    d = int(input())
    return
