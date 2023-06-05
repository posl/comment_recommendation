def main():
    # 读入数据
    K = int(input())
    A, B = map(int, input().split())
    # 将A，B转换为10进制
    A = int(str(A), K)
    B = int(str(B), K)
    # 计算并打印结果
    print(A*B)

if __name__ == '__main__':
    main()