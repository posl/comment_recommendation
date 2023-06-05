def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 计算答案
    ans = a + b + c
    ans = max(ans, a + b)
    ans = max(ans, b + c)
    ans = max(ans, c + a)
    # 打印答案
    print(ans)
main()
