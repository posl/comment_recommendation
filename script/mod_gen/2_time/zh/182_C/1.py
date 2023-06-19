def main():
    n = int(input())
    k = len(str(n))
    if k == 1:
        if n % 3 == 0:
            print(0)
        else:
            print(-1)
        exit()
    if k == 2:
        if n % 3 == 0:
            print(0)
        elif n % 3 == 1:
            if 1 in list(map(int, list(str(n)))):
                print(1)
            else:
                print(-1)
        else:
            if 2 in list(map(int, list(str(n)))):
                print(1)
            else:
                print(-1)
        exit()
    if k == 3:
        if n % 3 == 0:
            print(0)
        elif n % 3 == 1:
            if 1 in list(map(int, list(str(n)))):
                print(1)
            elif 2 in list(map(int, list(str(n)))):
                print(2)
            else:
                print(-1)
        else:
            if 2 in list(map(int, list(str(n)))):
                print(1)
            elif 1 in list(map(int, list(str(n)))):
                print(2)
            else:
                print(-1)
        exit()
    if n % 3 == 0:
        print(0)
    elif n % 3 == 1:
        if 1 in list(map(int, list(str(n)))):
            print(1)
        elif 2 in list(map(int, list(str(n)))):
            print(2)
        else:
            print(-1)
    else:
        if 2 in list(map(int, list(str(n)))):
            print(1)
        elif 1 in list(map(int, list(str(n)))):
            print(2)
        else:
            print(-1)

if __name__ == '__main__':
    main()