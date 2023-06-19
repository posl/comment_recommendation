def main():
    # 从标准输入读取字符串
    s = input()
    # 从0到9的所有数字正好出现一次，那么0到9的和减去字符串s的和，就是缺少的数字
    print(45 - sum(map(int, s)))
