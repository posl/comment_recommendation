def main():
    n = input()
    n = [int(x) for x in str(n)]
    n = n[::-1]
    n = sum(n)
    if n % 3 == 0:
        print(0)
    else:
        if len(n) == 1:
            print(-1)
        elif n % 3 == 1:
            if n.count(1) >= 1:
                print(1)
            elif n.count(4) >= 1:
                print(1)
            elif n.count(7) >= 1:
                print(1)
            elif n.count(2) >= 2:
                print(2)
            elif n.count(5) >= 2:
                print(2)
            elif n.count(8) >= 2:
                print(2)
            elif n.count(2) >= 1 and n.count(5) >= 1:
                print(2)
            elif n.count(2) >= 1 and n.count(8) >= 1:
                print(2)
            elif n.count(5) >= 1 and n.count(8) >= 1:
                print(2)
            elif n.count(3) >= 2:
                print(2)
            elif n.count(6) >= 2:
                print(2)
            elif n.count(9) >= 2:
                print(2)
            elif n.count(3) >= 1 and n.count(6) >= 1:
                print(2)
            elif n.count(3) >= 1 and n.count(9) >= 1:
                print(2)
            elif n.count(6) >= 1 and n.count(9) >= 1:
                print(2)
            elif n.count(4) >= 2:
                print(2)
            elif n.count(7) >= 2:
                print(2)
            elif n.count(1) >= 2:
                print(2)
            elif n.count(4) >= 1 and n.count(7) >= 1:
                print(2)
            elif n.count(1) >= 1 and n.count(4) >= 1:
                print(2)
            elif n.count(1) >= 1 and n.count(7) >= 1:
                print(2)
            else:
                print(-1)

if __name__ == '__main__':
    main()