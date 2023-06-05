def main():
    #输入
    n = int(input())
    h = list(map(int, input().split()))
    #计算
    max_move = 0
    move = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            move += 1
        else:
            move = 0
        if move > max_move:
            max_move = move
    #输出
    print(max_move)
