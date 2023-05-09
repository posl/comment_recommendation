def main():
    A,B = map(int,input().split())
    C = A+B
    if C == 3:
        print(3)
    elif C == 2:
        print(4)
    elif C == 1:
        print(2)
    elif C == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()