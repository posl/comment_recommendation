def solve():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 3:
        if int(s) % 8 == 0 or int(s[1] + s[2] + s[0]) % 8 == 0 or int(s[2] + s[0] + s[1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for i in range(112, 1000, 8):
        if i % 8 != 0:
            continue
        j = str(i)
        if len(j) < 3:
            continue
        dd = {}
        for c in j:
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
        ok = True
        for k, v in dd.items():
            if k not in d or d[k] < v:
                ok = False
                break
        if ok:
            print('Yes')
            return
    print('No')
