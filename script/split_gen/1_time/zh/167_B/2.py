def main():
    #读取输入
    a, b, c, k = map(int, input().split())
    #计算
    if k <= a:
        ans = k
    elif k <= a + b:
        ans = a
    else:
        ans = a - (k - a - b)
    #打印输出
    print(ans)
