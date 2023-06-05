def main():
    # 读取输入
    n = int(input())
    p = [int(i) for i in input().split()]
    # 计算答案
    ans = 0
    for i in range(n):
        if p[i] == (p[(i-1) % n] + 1) % n or p[i] == (p[(i+1) % n] + 1) % n:
            ans += 1
    # 输出答案
    print(ans)
