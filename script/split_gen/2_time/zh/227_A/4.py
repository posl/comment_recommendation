def main():
    # 输入
    n, k, a = map(int, input().split())
    #print(n, k, a)
    # 处理
    result = (k - (n - a + 1)) % n
    # 输出
    print(result)
