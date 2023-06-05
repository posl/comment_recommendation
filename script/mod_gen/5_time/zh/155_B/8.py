def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 检查条件
    for a in A:
        if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
            print("DENIED")
            return
    # 输出结果
    print("APPROVED")
main()
