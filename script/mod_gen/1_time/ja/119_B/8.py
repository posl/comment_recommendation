def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_, u_ = input().split()
        x.append(x_)
        u.append(u_)
    ans = 0
    for i in range(N):
        if u[i] == "JPY":
            ans += int(x[i])
        else:
            ans += float(x[i]) * 380000.0
    print(ans)

if __name__ == '__main__':
    main()