def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 求解并输出
    if pow(A, C) > pow(B, C):
        print(">")
    elif pow(A, C) < pow(B, C):
        print("<")
    else:
        print("=")

if __name__ == '__main__':
    main()