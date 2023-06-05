def main():
    # 读取输入
    k = int(input())
    # 算法开始
    a = 7
    for i in range(1, k + 1):
        if a % k == 0:
            print(i)
            return
        a = a * 10 + 7
    print(-1)
