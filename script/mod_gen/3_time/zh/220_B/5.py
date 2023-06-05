def main():
    # 读取数据
    k = int(input())
    a, b = input().split()
    # 从k进制转换为十进制
    a = int(a, k)
    b = int(b, k)
    # 乘法
    ans = a * b
    # 从十进制转换为k进制
    ans = str(ans)
    ans = int(ans, 10)
    print(ans)

if __name__ == '__main__':
    main()