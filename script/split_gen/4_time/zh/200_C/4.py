def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 用字典存储余数
    dic = {}
    for i in range(n):
        a[i] = a[i] % 200
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    # 计算结果
    ans = 0
    for i in dic:
        ans += dic[i]*(dic[i]-1)//2
    # 输出结果
    print(ans)
