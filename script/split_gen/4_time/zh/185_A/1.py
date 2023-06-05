def main():
    #输入
    a = list(map(int, input().split()))
    #处理
    a.sort()
    #输出
    if a[0] + a[1] + a[2] >= a[3]:
        print(3)
    elif a[0] + a[1] >= a[2] + a[3]:
        print(2)
    elif a[0] + a[1] >= a[3]:
        print(2)
    else:
        print(1)
