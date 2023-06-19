def main():
    x, y = input().split()
    if int(x) > int(y):
        if int(x) - int(y) <= 2:
            print("Yes")
        else:
            print("No")
    else:
        if int(y) - int(x) <= 2:
            print("Yes")
        else:
            print("No")
main()
