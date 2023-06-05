def main():
    #输入
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    #计算
    t = t % sum(a)
    #输出
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        else:
            t -= a[i]
