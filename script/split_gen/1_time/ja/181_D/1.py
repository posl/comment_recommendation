def solve():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0:
            print('Yes')
        elif int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    # 3桁以上の場合
    from collections import Counter
    c = Counter(s)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - c:
            print('Yes')
            return
    print('No')
