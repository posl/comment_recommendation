def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    if x == y:
        print("Yes")
    elif x == -y:
        print("Yes")
    elif x == 0 and y % 2 == 0:
        print("Yes")
    elif y == 0 and x % 2 == 0:
        print("Yes")
    else:
        print("No")
