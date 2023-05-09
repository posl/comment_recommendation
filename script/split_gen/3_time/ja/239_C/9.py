def main():
    x1, y1, x2, y2 = map(int, input().split())
    #print(x1, y1, x2, y2)
    #print(abs(x1-x2), abs(y1-y2))
    if abs(x1-x2) + abs(y1-y2) == 5:
        print("Yes")
    elif abs(x1-x2) + abs(y1-y2) == 3:
        print("Yes")
    elif abs(x1-x2) + abs(y1-y2) == 1:
        print("Yes")
    else:
        print("No")
