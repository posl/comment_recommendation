def main():
    n = int(input())
    a, p, x = [], [], []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    ans = 10000000000
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10000000000:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()