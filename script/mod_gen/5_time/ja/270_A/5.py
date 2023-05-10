def main():
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        print(0)
    elif A == 1 and B == 0:
        print(2)
    elif A == 0 and B == 1:
        print(2)
    elif A == 2 and B == 0:
        print(4)
    elif A == 0 and B == 2:
        print(4)
    elif A == 1 and B == 1:
        print(3)
    elif A == 2 and B == 1:
        print(5)
    elif A == 1 and B == 2:
        print(5)
    elif A == 2 and B == 2:
        print(6)
    elif A == 3 and B == 0:
        print(6)
    elif A == 0 and B == 3:
        print(6)
    elif A == 3 and B == 1:
        print(7)
    elif A == 1 and B == 3:
        print(7)
    elif A == 3 and B == 2:
        print(8)
    elif A == 2 and B == 3:
        print(8)
    elif A == 3 and B == 3:
        print(9)

if __name__ == '__main__':
    main()