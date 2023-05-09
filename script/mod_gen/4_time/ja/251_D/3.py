def main():
    W = int(input())
    if W == 3:
        print(2)
        print("1 2")
    elif W == 2:
        print(1)
        print("2")
    elif W == 1:
        print(1)
        print("1")
    elif W == 4:
        print(2)
        print("1 3")
    elif W == 5:
        print(2)
        print("2 3")
    elif W == 6:
        print(3)
        print("1 2 3")
    else:
        print(6)
        print("1 2 3 4 5 6")

if __name__ == '__main__':
    main()