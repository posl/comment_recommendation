def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    if x1 == x2 or y1 == y2:
        print("Yes")
        return
    if abs(x1 - x2) == abs(y1 - y2):
        print("Yes")
        return
    print("No")
