def main():
    # 读取输入
    s = input()
    # 输出结果
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")
