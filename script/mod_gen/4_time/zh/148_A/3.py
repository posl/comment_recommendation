def problems148_a():
    # 读取输入
    a = int(input())
    b = int(input())
    # 判断a,b的值
    if a == 1 and b == 2:
        print(3)
    elif a == 2 and b == 1:
        print(3)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 2:
        print(1)
    elif a == 3 and b == 1:
        print(2)
    elif a == 1 and b == 3:
        print(2)

if __name__ == '__main__':
    problems148_a()