def get_num():
    while True:
        try:
            num = input().split(' ')
            num = [int(x) for x in num]
            if num[0] != len(num) - 2:
                print("输入的数值不符合要求，请重新输入")
                continue
            else:
                break
        except:
            print("输入的数值不符合要求，请重新输入")
    return num
