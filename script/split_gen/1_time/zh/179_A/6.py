def main():
    # 读取输入
    s = input()
    # 根据题意，判断单词s是否以s结尾
    if s[-1] == 's':
        # 如果是，则在单数形式的末尾加上es
        print(s + 'es')
    else:
        # 如果不是，则在单数形式的后面加上s
        print(s + 's')
