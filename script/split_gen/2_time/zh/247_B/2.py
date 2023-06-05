def main():
    # 输入
    S = input()
    # 处理
    S = S.replace('1', '2').replace('0', '1').replace('2', '0')
    # 输出
    print(S)
