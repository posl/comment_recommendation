def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 and x2 == y2:
        print("No")
        return
    if x1 == x2 and y1 == y2:
        print("Yes")
        return
    if x1 == y1 or x2 == y2:
        print("No")
        return
    if x1 == y2 or x2 == y1:
        print("No")
        return
    print("Yes")
