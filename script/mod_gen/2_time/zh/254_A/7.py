def main():
    num = input()
    if len(num) < 3:
        print('0' + num)
    else:
        print(num[-2:])

if __name__ == '__main__':
    main()