def main():
    # 读入数据
    k = int(input())
    # 处理数据
    ans = ""
    for i in range(k):
        ans += chr(ord('A') + i)
    # 输出结果
    print(ans)
