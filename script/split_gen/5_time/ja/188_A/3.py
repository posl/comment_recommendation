def main():
    x, y = map(int, input().split())
    if x > y:
        if x - y < 3:
            print("Yes")
        else:
            print("No")
    elif x < y:
        if y - x < 3:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
