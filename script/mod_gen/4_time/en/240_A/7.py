def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a == 1 and b == 2:
        print("Yes")
    elif a == 1 and b == 3:
        print("Yes")
    elif a == 1 and b == 4:
        print("Yes")
    elif a == 1 and b == 5:
        print("Yes")
    elif a == 2 and b == 3:
        print("Yes")
    elif a == 2 and b == 4:
        print("Yes")
    elif a == 2 and b == 5:
        print("Yes")
    elif a == 3 and b == 4:
        print("Yes")
    elif a == 3 and b == 5:
        print("Yes")
    elif a == 4 and b == 5:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()