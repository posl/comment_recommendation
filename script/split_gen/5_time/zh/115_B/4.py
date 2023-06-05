def get_input():
    #输入
    N = int(input())
    p = [0] * N
    for i in range(N):
        p[i] = int(input())
    return N, p
