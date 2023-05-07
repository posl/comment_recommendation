def main():
    n = input()
    if len(n) == 4:
        print(n)
    elif len(n) == 3:
        print("0" + n)
    elif len(n) == 2:
        print("00" + n)
    elif len(n) == 1:
        print("000" + n)

if __name__ == '__main__':
    main()