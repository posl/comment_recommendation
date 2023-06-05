def main():
    n = int(input())
    # 读取数据
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    # 判断是否能购买
    flag = False
    for i in range(n):
        if x[i] > 0:
            flag = True
            break
    if flag == False:
        print(-1)
        return
    # 计算最低资金量
    min_price = 10**9
    for i in range(n):
        if x[i] > 0 and p[i] < min_price:
            min_price = p[i]
    print(min_price)
