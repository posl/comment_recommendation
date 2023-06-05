def main():
    #输入
    N, M, X, T, D = map(int, input().split())
    #处理
    for i in range(X, M):
        T += D
    #输出
    print(T)
