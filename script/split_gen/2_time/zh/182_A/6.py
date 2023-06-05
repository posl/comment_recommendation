def solve():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    cnt = [0] * 10
    for i in s:
        cnt[int(i)] += 1
    for i in range(112, 1000, 8):
        tmp = [0] * 10
        tmp[0] = cnt[0]
        for j in range(1, 10):
            tmp[j] = cnt[j]
        for j in str(i):
            tmp[int(j)] -= 1
        if all(x >= 0 for x in tmp):
            print('Yes')
            return
    print('No')
