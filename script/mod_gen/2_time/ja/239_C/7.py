def main():
    x1, y1, x2, y2 = map(int, input().split())
    #print(x1, y1, x2, y2)
    if x1 == x2:
        print("Yes")
        return
    if y1 == y2:
        print("Yes")
        return
    if x1 + y1 == x2 + y2:
        print("Yes")
        return
    if x1 - y1 == x2 - y2:
        print("Yes")
        return
    print("No")
main()
