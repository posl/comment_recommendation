def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 逻辑处理
    if A == B and B == C:
        print("No")
    elif A == B or B == C or A == C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()