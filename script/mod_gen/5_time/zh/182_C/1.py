def main():
    n = int(input())
    if n%3 == 0:
        print(0)
        return
    elif n%3 == 1:
        if n%10 == 1:
            print(1)
            return
        elif n%10 == 4:
            print(1)
            return
        elif n%10 == 7:
            print(1)
            return
        else:
            print(2)
            return
    elif n%3 == 2:
        if n%10 == 2:
            print(1)
            return
        elif n%10 == 5:
            print(1)
            return
        elif n%10 == 8:
            print(1)
            return
        else:
            print(2)
            return
    else:
        print(-1)
        return

if __name__ == '__main__':
    main()