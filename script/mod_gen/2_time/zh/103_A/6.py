def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())
    # 请在此处编写您的代码（可选）
    # 输出结果
    print(min(abs(a1-a2)+abs(a2-a3),abs(a1-a3)+abs(a2-a3),abs(a1-a2)+abs(a1-a3)))

if __name__ == '__main__':
    main()