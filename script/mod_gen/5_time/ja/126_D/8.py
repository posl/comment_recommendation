def main():
    n = int(input())
    u = []
    v = []
    w = []
    for i in range(n-1):
        u_i, v_i, w_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
        w.append(w_i)
    ans = [0] * n
    for i in range(n-1):
        if w[i] % 2 == 0:
            ans[v[i]-1] = ans[u[i]-1]
        else:
            ans[v[i]-1] = 1 - ans[u[i]-1]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()