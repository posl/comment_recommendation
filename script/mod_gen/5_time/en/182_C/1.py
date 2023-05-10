def main():
    n = int(input())
    if n%3 == 0:
        print(0)
        return
    if n%3 == 1:
        if n%10 == 1:
            if n%100 == 11:
                print(2)
            else:
                print(1)
        elif n%10 == 4:
            if n%100 == 14:
                print(2)
            else:
                print(1)
        elif n%10 == 7:
            if n%100 == 17:
                print(2)
            else:
                print(1)
        else:
            print(-1)
    else:
        if n%10 == 2:
            if n%100 == 22:
                print(2)
            else:
                print(1)
        elif n%10 == 5:
            if n%100 == 25:
                print(2)
            else:
                print(1)
        elif n%10 == 8:
            if n%100 == 28:
                print(2)
            else:
                print(1)
        else:
            print(-1)

if __name__ == '__main__':
    main()