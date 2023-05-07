def main():
    # 入力
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(x_i)
        u.append(u_i)
    # 処理
    ans = 0
    for i in range(N):
        if u[i] == 'JPY':
            ans += int(x[i])
        else:
            ans += float(x[i])*380000.0
    # 出力
    print(ans)
