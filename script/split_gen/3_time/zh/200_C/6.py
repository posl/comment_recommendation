def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 保存余数的计数器
    r = [0] * 200
    # 计算余数
    for a in A:
        r[a % 200] += 1
    # 计算配对数
    ans = 0
    for i in range(200):
        ans += r[i] * (r[i] - 1) // 2
    # 输出答案
    print(ans)
