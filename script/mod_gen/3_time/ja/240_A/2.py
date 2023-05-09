def main():
    a, b = map(int, input().split())
    if a == 1:
        if b == 2 or b == 3:
            print("Yes")
        else:
            print("No")
    elif a == 2:
        if b == 4 or b == 5:
            print("Yes")
        else:
            print("No")
    elif a == 3:
        if b == 6 or b == 7:
            print("Yes")
        else:
            print("No")
    elif a == 4:
        if b == 8 or b == 9:
            print("Yes")
        else:
            print("No")
    elif a == 5:
        if b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 6:
        if b == 8 or b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 7:
        if b == 9 or b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 8:
        if b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 9:
        if b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 10:
        print("Yes")
main()

if __name__ == '__main__':
    main()