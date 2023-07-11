def main():
    # 读取输入
    s = input()
    # 处理
    if s[-1] == 's':
        s += 'es'
    else:
        s += 's'
