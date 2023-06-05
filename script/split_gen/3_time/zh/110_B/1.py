def main():
    # 输入
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 逻辑处理
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    # 输出
    if x[-1] < y[0] and x[-1] < Y and y[0] > X:
        print('No War')
    else:
        print('War')
