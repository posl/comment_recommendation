def main():
    A = int(input())
    B = int(input())
    C = 0
    if A == 1:
        if B == 2:
            C = 3
        elif B == 3:
            C = 2
    elif A == 2:
        if B == 1:
            C = 3
        elif B == 3:
            C = 1
    elif A == 3:
        if B == 1:
            C = 2
        elif B == 2:
            C = 1
    print(C)
main()

if __name__ == '__main__':
    main()