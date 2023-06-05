def main():
    # 读入输入
    C = input()
    # 判断并输出
    if C[0] == C[1] and C[1] == C[2]:
        print('Won')
    else:
        print('Lost')
