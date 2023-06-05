def main():
    s = input()
    num = 0
    for i in s:
        if i == '+':
            num += 1
        else:
            num -= 1
    print(num)

if __name__ == '__main__':
    main()