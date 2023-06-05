def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x*(j-i+1))
    # 输出答案
    print(ans)
