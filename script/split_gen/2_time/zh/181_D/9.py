def solve():
    s = input()
    if len(s) <= 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    cnt = [0] * 10
    for c in s:
        cnt[int(c)] += 1
    for i in range(112, 1000, 8):
        t = [0] * 10
        t[i % 10] += 1
        t[(i // 10) % 10] += 1
        t[i // 100] += 1
        if all(t[j] <= cnt[j] for j in range(10)):
            print('是')
            return
    print('否')
solve()
