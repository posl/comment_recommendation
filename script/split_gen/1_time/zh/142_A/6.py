def main():
    # 读取输入
    n = int(input())
    # 解决问题
    ans = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            ans += 1
    # 输出答案
    print(ans/n)
