def main():
    # 读取输入
    n = int(input())
    s = input()
    # 计数
    count = 0
    # 遍历
    for i in range(n - 2):
        # 判断
        if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
            count += 1
    # 输出
    print(count)
