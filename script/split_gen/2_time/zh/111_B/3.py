def problems111_a():
    n = input("请输入一个三位数：")
    if 111 <= int(n) <= 999:
        result = ''
        for i in n:
            if i == '1':
                result += '9'
            else:
                result += '1'
        print(result)
    else:
        print("输入的数字不符合要求，请重新输入！")
        problems111_a()
problems111_a()
