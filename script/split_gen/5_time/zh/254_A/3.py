def getlast2(n):
    if n < 100 or n > 999:
        print("输入必须是3位数")
        return
    print(n % 100)
