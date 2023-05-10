def main():
    W = int(input())
    if W == 3:
        print(2)
        print(1, 2)
    elif W == 2 or W == 4:
        print(2)
        print(1, 3)
    elif W == 1:
        print(1)
        print(1)
    else:
        print(6)
        print(2, 5, 1, 2, 5, 1)

if __name__ == '__main__':
    main()