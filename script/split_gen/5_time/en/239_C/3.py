def main():
    # input
    x1, y1, x2, y2 = map(int, input().split())
    # compute
    # output
    if x1 == x2 and y1 == y2:
        print("No")
    else:
        if abs(x1 - x2) == abs(y1 - y2):
            print("Yes")
        else:
            print("No")
