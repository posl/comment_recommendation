def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append((t, d))
    Sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    t_set = set()
    t_list = []
    for t, d in Sushi[:K]:
        ans += d
        if t not in t_set:
            t_list.append(t)
            t_set.add(t)
    ans += len(t_list)**2
    c = len(t_list)
    for i in range(K, N):
        if Sushi[i][0] in t_set:
            continue
        t, d = Sushi[i]
        t_set.add(t)
        t_list.append(t)
        ans += d - Sushi[c][1]
        c += 1
        ans += 2*len(t_list) - 1
        if ans > 10**18:
            ans = 10**18
    print(ans)

if __name__ == '__main__':
    main()