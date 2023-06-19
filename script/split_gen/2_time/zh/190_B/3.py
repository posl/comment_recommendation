def main():
    #读取数据
    n, s, d = map(int, input().split())
    x = []
    y = []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #判断是否可以造成伤害
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')
