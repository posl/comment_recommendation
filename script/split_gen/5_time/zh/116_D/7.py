def main():
    n, k = map(int, input().split())
    t = []
    d = []
    for i in range(n):
        t_i, d_i = map(int, input().split())
        t.append(t_i)
        d.append(d_i)
    sushi = []
    for i in range(n):
        sushi.append([d[i], t[i]])
    sushi.sort(reverse=True)
    eat = []
    eat_kind = []
    for i in range(k):
        eat.append(sushi[i][0])
        if sushi[i][1] not in eat_kind:
            eat_kind.append(sushi[i][1])
    ans = sum(eat) + len(eat_kind)**2
    print(ans)
