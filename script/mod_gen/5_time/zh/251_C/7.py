def main():
    n = input()
    d = {}
    for i in range(n):
        s, t = raw_input().split()
        if s in d:
            d[s].append((i, int(t)))
        else:
            d[s] = [(i, int(t))]
    for k in d:
        d[k].sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for k in d:
        if len(d[k]) > 1 and d[k][0][1] == d[k][1][1]:
            continue
        if d[k][0][1] > d[k][1][1]:
            ans = max(ans, d[k][0][0])
    print ans + 1

if __name__ == '__main__':
    main()