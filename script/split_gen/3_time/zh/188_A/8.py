def main():
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        if x - y < 3:
            print("Yes")
        else:
            print("No")
    else:
        if y - x < 3:
            print("Yes")
        else:
            print("No")
