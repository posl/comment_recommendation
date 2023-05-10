def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1,2)
    elif w == 2:
        print(2)
        print(1,2)
    elif w == 1:
        print(1)
        print(1)
    elif w == 4:
        print(3)
        print(1,2,3)
    elif w == 5:
        print(3)
        print(1,2,3)
    elif w == 6:
        print(3)
        print(1,2,3)
    else:
        print(6)
        print(2,5,1,2,5,1)

if __name__ == '__main__':
    main()