def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    min_p = 10**9
    for i in range(n):
        if x[i] > 0:
            if p[i] < min_p:
                min_p = p[i]
    if min_p == 10**9:
        min_p = -1
    print(min_p)

if __name__ == '__main__':
    main()