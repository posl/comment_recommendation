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
    min_p = 1000000000
    for i in range(n):
        if x[i] > 0:
            min_p = min(min_p, p[i])
    if min_p == 1000000000:
        print(-1)
        return
    print(min_p)
