def main():
    # 读取输入
    N = int(input())
    # 计算并输出结果
    count = 0
    for i in range(1, N + 1):
        # 将数字转换成字符串，然后判断奇偶
        if str(i).count('1') % 2 == 1:
            count += 1
    print(count)
