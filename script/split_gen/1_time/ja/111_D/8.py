def main():
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]
    if n == 1:
        print(1)
        print(1, 1)
        print("R")
        return
    if n == 2:
        x1, y1 = xys[0]
        x2, y2 = xys[1]
        if x1 == x2 and y1 == y2:
            print(2)
            print(1, 1)
            print("RU")
            print("UR")
            return
        else:
            print(-1)
            return
    if n == 3:
        x1, y1 = xys[0]
        x2, y2 = xys[1]
        x3, y3 = xys[2]
        if x1 == x2 and x2 == x3 and y1 == y2 and y2 == y3:
            print(3)
            print(1, 1, 1)
            print("RUU")
            print("URU")
            print("UUR")
            return
        else:
            print(-1)
            return
    if n == 4:
        x1, y1 = xys[0]
        x2, y2 = xys[1]
        x3, y3 = xys[2]
        x4, y4 = xys[3]
        if x1 == x2 and x2 == x3 and x3 == x4 and y1 == y2 and y2 == y3 and y3 == y4:
            print(4)
            print(1, 1, 1, 1)
            print("RUUU")
            print("URUU")
            print("UURU")
            print("UUUR")
            return
        else:
            print(-1)
            return
    if n == 5:
        x1, y1 = xys[0]
        x2, y2 = xys[1]
        x3, y3 = xys[2]
        x4, y4 = xys[3]
        x5, y5 = xys[4]
        if x1 == x2 and x2 == x3 and x3 == x4 and x4 == x5 and y1
