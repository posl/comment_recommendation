def main():
    #读入数据
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X * X + Y * Y <= D * D:
            cnt += 1
    print(cnt)
