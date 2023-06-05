def main():
    num = input()
    num1 = int(num[0] + num[1] + num[2])
    num2 = int(num[0] + num[2] + num[1])
    num3 = int(num[1] + num[0] + num[2])
    num4 = int(num[1] + num[2] + num[0])
    num5 = int(num[2] + num[0] + num[1])
    num6 = int(num[2] + num[1] + num[0])
    print(num1 + num2 + num3 + num4 + num5 + num6)

if __name__ == '__main__':
    main()