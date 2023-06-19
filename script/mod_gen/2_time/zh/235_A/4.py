def main():
    num = input()
    if len(num) == 3:
        num = int(num)
        x = num // 100
        y = (num // 10) % 10
        z = num % 10
        print(x + y + z + (x * 10 + y) + (y * 10 + z) + (z * 10 + x))
    else:
        print("输入不合法")

if __name__ == '__main__':
    main()