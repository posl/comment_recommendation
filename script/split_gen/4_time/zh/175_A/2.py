def main():
    # 读取输入
    s = input()
    # 处理
    # 通过字符串的count方法，计算R出现的次数
    # 通过max方法，计算最大值
    max_count = max(s.count('R'), s.count('S'))
    # 输出结果
    print(max_count)
