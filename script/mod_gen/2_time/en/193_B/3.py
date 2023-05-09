def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        ai, pi, xi = map(int, input().split())
        a.append(ai)
        p.append(pi)
        x.append(xi)
    min_p = 10**9
    for i in range(n):
        if x[i] > a[i]:
            min_p = min(min_p, p[i])
    if min_p == 10**9:
        print(-1)
    else:
        print(min_p)

if __name__ == '__main__':
    main()