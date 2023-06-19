def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 算法
    if A >= B + C:
        print(0)
    else:
        print(C - (A - B))

if __name__ == '__main__':
    main()