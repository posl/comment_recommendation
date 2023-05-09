def problem180_b():
    N = int(input())
    x = list(map(int, input().split()))
    # マンハッタン距離
    m = 0
    for i in range(N):
        m += abs(x[i])
    # ユークリッド距離
    u = 0
    for i in range(N):
        u += x[i]**2
    u = u**0.5
    # チェビシェフ距離
    c = abs(x[0])
    for i in range(N):
        if c < abs(x[i]):
            c = abs(x[i])
    print(m)
    print(u)
    print(c)

if __name__ == '__main__':
    problem180_b()