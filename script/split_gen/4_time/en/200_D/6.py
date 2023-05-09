def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 200
    mod_a = [x % mod for x in a]
    d = {}
    for i, x in enumerate(mod_a):
        if x not in d:
            d[x] = [i]
        else:
            d[x].append(i)
    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(1, v[0] + 1)
            print(1, v[1] + 1)
            return
    for i in range(mod):
        for j in range(i + 1, mod):
            if i in d and j in d:
                print('Yes')
                print(1, d[i][0] + 1)
                print(2, d[i][1] + 1, d[j][0] + 1)
                return
    print('No')
