def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    ans = 0
    for i in range(N):
        if u[i] == 'BTC':
            ans += x[i] * 380000
        else:
            ans += x[i]
    print(ans)
