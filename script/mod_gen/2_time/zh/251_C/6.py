def main():
    n = int(input())
    d = dict()
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in d:
            d[s].append((t, i))
        else:
            d[s] = [(t, i)]
    for k in d.keys():
        d[k].sort()
    ans = -1
    max_t = 0
    for k in d.keys():
        if len(d[k]) >= 2:
            if d[k][-1][0] > max_t:
                max_t = d[k][-1][0]
                ans = d[k][-1][1]
        if d[k][0][0] > max_t:
            max_t = d[k][0][0]
            ans = d[k][0][1]
    print(ans + 1)

if __name__ == '__main__':
    main()