def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 解决问题
    if a * c <= b:
        ans = c
    else:
        ans = b // a
    # 输出结果
    print(ans)
