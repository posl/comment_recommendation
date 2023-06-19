def main():
    #输入
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    #处理
    sum = 0
    for i in range(N):
        if u[i] == 'BTC':
            sum += x[i] * 380000
        elif u[i] == 'JPY':
            sum += x[i]
    #输出
    print(sum)
