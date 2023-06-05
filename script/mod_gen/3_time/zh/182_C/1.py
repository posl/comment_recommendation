def main():
    n = input()
    k = len(n)
    if k == 1:
        if int(n) % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    if k == 2:
        if int(n) % 3 == 0:
            print(0)
        elif int(n[0]) % 3 == 0:
            print(1)
        elif int(n[1]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 3:
        if int(n) % 3 == 0:
            print(0)
        elif int(n[0]) % 3 == 0:
            print(2)
        elif int(n[1]) % 3 == 0:
            print(1)
        elif int(n[2]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 4:
        if int(n) % 3 == 0:
            print(0)
        elif int(n[0]) % 3 == 0:
            print(3)
        elif int(n[1]) % 3 == 0:
            print(2)
        elif int(n[2]) % 3 == 0:
            print(1)
        elif int(n[3]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 5:
        if int(n) % 3 == 0:
            print(0)
        elif int(n[0]) % 3 == 0:
            print(4)
        elif int(n[1]) % 3 == 0:
            print(3)
        elif int(n[2]) % 3 == 0:
            print(2)
        elif int(n[3]) % 3 == 0:
            print(1)
        elif int(n[4]) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 6:
        if int(n) % 3 == 0:
            print(0)
        elif int(n[0]) % 3 == 0:
            print(5)
        elif int

if __name__ == '__main__':
    main()