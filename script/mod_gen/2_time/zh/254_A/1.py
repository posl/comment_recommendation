def printLastTwoDigits():
    n = int(input())
    if n < 100 or n > 999:
        print("输入错误")
    else:
        print(n % 100)

if __name__ == '__main__':
    printLastTwoDigits()