def main():
    a = int(input())
    if a % 10 == 2 or a % 10 == 4 or a % 10 == 5 or a % 10 == 7 or a % 10 == 9:
        print("hon")
    elif a % 10 == 0 or a % 10 == 1 or a % 10 == 6 or a % 10 == 8:
        print("pon")
    else:
        print("bon")

if __name__ == '__main__':
    main()