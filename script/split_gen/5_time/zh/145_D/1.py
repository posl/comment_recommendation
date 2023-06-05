def main():
    x,y = map(int,input().split())
    if x < y:
        x,y = y,x
    if x == 2 and y == 2:
        print(0)
        return
    if x == 1 and y == 2:
        print(1)
        return
    if x == 2 and y == 3:
        print(2)
        return
    if x == 3 and y == 3:
        print(2)
        return
    if x == 3 and y == 2:
        print(2)
        return
    if x == 3 and y == 1:
        print(1)
        return
    a = x - y
    b = y - 1
    if a % 3 == 0:
        a = a // 3
        b = b // 3
    else:
        a = a // 3 + 1
        b = b // 3 + 1
    print(a+b)
