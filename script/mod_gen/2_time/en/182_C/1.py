def main():
    n = input()
    n = [int(i) for i in n]
    n = sum(n)
    if n % 3 == 0:
        print(0)
    elif len(n) == 1:
        print(-1)
    elif n % 3 == 1:
        if 1 in n or 4 in n or 7 in n:
            print(1)
        elif 2 in n or 5 in n or 8 in n:
            print(2)
        else:
            print(-1)
    elif n % 3 == 2:
        if 2 in n or 5 in n or 8 in n:
            print(1)
        elif 1 in n or 4 in n or 7 in n:
            print(2)
        else:
            print(-1)

if __name__ == '__main__':
    main()