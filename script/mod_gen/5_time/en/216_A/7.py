def main():
    num = input()
    num = num.split(".")
    if int(num[1]) >= 0 and int(num[1]) <= 2:
        print(num[0] + "-")
    elif int(num[1]) >= 3 and int(num[1]) <= 6:
        print(num[0])
    elif int(num[1]) >= 7 and int(num[1]) <= 9:
        print(num[0] + "+")

if __name__ == '__main__':
    main()