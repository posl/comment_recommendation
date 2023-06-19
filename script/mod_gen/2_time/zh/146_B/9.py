def problem146_b():
    # 获取输入
    N = int(input())
    S = input()
    # 处理
    result = ""
    for s in S:
        result += chr(ord('A') + (ord(s) - ord('A') + N) % 26)
    # 输出结果
    print(result)

if __name__ == '__main__':
    problem146_b()