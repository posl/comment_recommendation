def main():
    # 读取输入
    input = raw_input()
    input = input.split()
    input = [int(i) for i in input]
    n = input[0]
    r = input[1]
    # 计算
    if n >= 10:
        print r
    else:
        print r + 100 * (10 - n)
