def main():
    # 输入
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # 判断
    sum = 0
    for i in range(N):
        if (i % 2 == 0):
            sum += b[i]
        else:
            sum += a[i]
    if (sum >= X):
        print("Yes")
    else:
        print("No")
