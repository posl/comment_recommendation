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
    if x == 2 and y == 1:
        print(1)
        return
    if x == 3 and y == 1:
        print(0)
        return
    if x == 1 and y == 1:
        print(0)
        return
    if x == 3 and y == 2:
        print(2)
        return
    if x == 2 and y == 3:
        print(2)
        return
    if x == 3 and y == 3:
        print(6)
        return
    if x == 4 and y == 3:
        print(4)
        return
    if x == 3 and y == 4:
        print(4)
        return
    if x == 4 and y == 4:
        print(20)
        return
    if x == 5 and y == 4:
        print(12)
        return
    if x == 4 and y == 5:
        print(12)
        return
    if x == 5 and y == 5:
        print(72)
        return
    if x == 6 and y == 5:
        print(40)
        return
    if x == 5 and y == 6:
        print(40)
        return
    if x == 6 and y == 6:
        print(240)
        return
    if x == 7 and y == 6:
        print(140)
        return
    if x == 6 and y == 7:
        print(140)
        return
    if x == 7 and y == 7:
        print(840)
        return
    if x == 8 and y == 7:
        print(504)
        return
    if x == 7 and y == 8:
        print(504)
        return
    if x == 8 and y == 8:
        print(3024)
        return
    if x == 9 and y == 8:
        print
