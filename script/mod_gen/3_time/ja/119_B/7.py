def main():
    #入力
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(int(x_i) if u_i == 'JPY' else float(x_i))
        u.append(u_i)
    #計算
    ans = 0
    for i in range(N):
        if u[i] == 'JPY':
            ans += x[i]
        else:
            ans += x[i] * 380000.0
    #出力
    print(ans)

if __name__ == '__main__':
    main()