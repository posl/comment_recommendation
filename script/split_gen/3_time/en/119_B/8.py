def main():
    N = int(input())
    x = []
    u = []
    for _ in range(N):
        x_, u_ = input().split()
        x.append(float(x_))
        u.append(u_)
    
    ans = 0
    for i in range(N):
        if u[i] == 'JPY':
            ans += x[i]
        elif u[i] == 'BTC':
            ans += x[i] * 380000.0
    
    print(ans)
