def main():
    Y = int(input())
    while Y < 2000 or Y > 3000:
        print('输入的年份不在范围内，请重新输入！')
        Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

if __name__ == '__main__':
    main()