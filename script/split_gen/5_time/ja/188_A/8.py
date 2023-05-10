def main():
    x, y = map(int, input().split())
    if x > y:
        if x - y <= 2:
            print("Yes")
        else:
            print("No")
    else:
        if y - x <= 2:
            print("Yes")
        else:
            print("No")
