def main():
    A = int(input())
    B = int(input())
    if A == 1 and B == 2:
        print(3)
    elif A == 2 and B == 1:
        print(3)
    elif A == 3 and B == 1:
        print(2)
    elif A == 1 and B == 3:
        print(2)
    elif A == 2 and B == 3:
        print(1)
    elif A == 3 and B == 2:
        print(1)

if __name__ == '__main__':
    main()