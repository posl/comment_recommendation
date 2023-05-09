def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 3 == 0:
        print(0)
    elif len(n) == 1:
        print(-1)
    elif len(n) == 2:
        if sum % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        if sum % 3 == 0:
            print(0)
        elif sum % 3 == 1:
            if n.count("1") > 0 or n.count("4") > 0 or n.count("7") > 0:
                if len(n) == 3:
                    print(-1)
                else:
                    print(1)
            elif n.count("2") > 1 or n.count("5") > 1 or n.count("8") > 1:
                print(2)
            elif n.count("2") > 0 or n.count("5") > 0 or n.count("8") > 0:
                if len(n) == 4:
                    print(-1)
                else:
                    print(2)
            else:
                print(3)
        else:
            if n.count("2") > 0 or n.count("5") > 0 or n.count("8") > 0:
                if len(n) == 3:
                    print(-1)
                else:
                    print(1)
            elif n.count("1") > 1 or n.count("4") > 1 or n.count("7") > 1:
                print(2)
            elif n.count("1") > 0 or n.count("4") > 0 or n.count("7") > 0:
                if len(n) == 4:
                    print(-1)
                else:
                    print(2)
            else:
                print(3)

if __name__ == '__main__':
    main()