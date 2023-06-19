def main():
    # 读入数据
    r, c = input().split()
    r = int(r)
    c = int(c)
    # 计算结果
    if r % 2 == 0:
        if c % 2 == 0:
            print("black")
        else:
            print("white")
    else:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
main()
