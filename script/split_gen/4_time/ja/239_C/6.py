def main():
    x_1,y_1,x_2,y_2 = map(int,input().split())
    if x_1 == x_2 and y_1 == y_2:
        print("No")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
        return
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 10:
        print("Yes")
        return
    if x_1 == x_2:
        if abs(y_1 - y_2) == 5:
            print("Yes")
            return
        if abs(y_1 - y_2) == 10:
            print("Yes")
            return
    if y_1 == y_2:
        if abs(x_1 - x_2) == 5:
            print("Yes")
            return
        if abs(x_1 - x_2) == 10:
            print("Yes")
            return
    print("No")
    return
