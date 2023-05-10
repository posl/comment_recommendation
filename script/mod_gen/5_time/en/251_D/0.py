def main():
    W = int(input())
    if W == 1:
        print(1)
        print(1)
    elif W == 2:
        print(2)
        print(1,1)
    elif W == 3:
        print(2)
        print(1,2)
    elif W == 4:
        print(3)
        print(1,2,1)
    elif W == 5:
        print(3)
        print(1,2,2)
    elif W == 6:
        print(3)
        print(1,2,3)
    elif W == 7:
        print(3)
        print(1,2,4)
    elif W == 8:
        print(4)
        print(1,2,2,3)
    elif W == 9:
        print(4)
        print(1,2,2,4)
    elif W == 10:
        print(4)
        print(1,2,3,4)
    elif W == 11:
        print(4)
        print(1,2,3,5)
    elif W == 12:
        print(4)
        print(1,2,3,6)
    else:
        print(5)
        print(1,2,3,4,5)

if __name__ == '__main__':
    main()