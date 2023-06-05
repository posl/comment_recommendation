def main():
    # 读取一行输入的字符串
    s = input()
    # 判断字符串中的所有字符是否相同
    if s[0] == s[1] and s[1] == s[2]:
        print('Won')
    else:
        print('Lost')
main()
