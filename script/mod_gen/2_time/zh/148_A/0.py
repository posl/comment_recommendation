def main():
    A = int(input())
    B = int(input())
    if A == 1:
        if B == 2:
            print(3)
        else:
            print(2)
    elif A == 2:
        if B == 1:
            print(3)
        else:
            print(1)
    elif A == 3:
        if B == 1:
            print(2)
        else:
            print(1)

if __name__ == '__main__':
    main()