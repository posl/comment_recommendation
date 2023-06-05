def buy_snuke():
    n = int(input())
    a_list = []
    p_list = []
    x_list = []
    for i in range(n):
        a, p, x = map(int, input().split())
        a_list.append(a)
        p_list.append(p)
        x_list.append(x)
    min_p = 10**9
    for i in range(n):
        if x_list[i] > 0:
            if p_list[i] < min_p:
                min_p = p_list[i]
    if min_p == 10**9:
        return -1
    else:
        return min_p
print(buy_snuke())
