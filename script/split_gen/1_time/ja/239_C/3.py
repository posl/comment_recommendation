def main():
    x1, y1, x2, y2 = map(int, input().split())
    #x1, y1, x2, y2 = 0, 0, 3, 3
    #x1, y1, x2, y2 = 0, 1, 2, 3
    #x1, y1, x2, y2 = 1000000000, 1000000000, 999999999, 999999999
    x = x2 - x1
    y = y2 - y1
    if x == 0 and y == 0:
        print("No")
    elif x == 0 or y == 0:
        print("Yes")
    elif x == y or x == -y:
        print("Yes")
    else:
        print("No")
