def main():
    a, b = map(int, input().split())
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 4 or a == 6 or a == 9:
        if b == 4 or b == 6 or b == 9:
            print("Yes")
        else:
            print("No")
    elif a == 2:
        if b == 2:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()