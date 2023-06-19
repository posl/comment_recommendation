def main():
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] > w:
        print(0)
        return
    if n == 1:
        if a[0] <= w:
            print(1)
        else:
            print(0)
        return
    if n == 2:
        if a[0] + a[1] <= w:
            print(3)
        elif a[0] <= w:
            print(2)
        else:
            print(1)
        return
    if n == 3:
        if a[0] + a[1] + a[2] <= w:
            print(7)
        elif a[0] + a[1] <= w:
            print(6)
        elif a[0] + a[2] <= w:
            print(5)
        elif a[1] + a[2] <= w:
            print(4)
        elif a[0] <= w:
            print(3)
        elif a[1] <= w:
            print(2)
        elif a[2] <= w:
            print(1)
        else:
            print(0)
        return
    if n == 4:
        if a[0] + a[1] + a[2] + a[3] <= w:
            print(15)
        elif a[0] + a[1] + a[2] <= w:
            print(14)
        elif a[0] + a[1] + a[3] <= w:
            print(13)
        elif a[0] + a[2] + a[3] <= w:
            print(12)
        elif a[1] + a[2] + a[3] <= w:
            print(11)
        elif a[0] + a[1] <= w:
            print(10)
        elif a[0] + a[2] <= w:
            print(9)
        elif a[0] + a[3] <= w:
            print(8)
        elif a[1] + a[2] <= w:
            print(7)
        elif a[1] + a[3] <= w:
            print(6)
        elif a[2]
