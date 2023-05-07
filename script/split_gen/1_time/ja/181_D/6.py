def solve():
    from collections import Counter
    s = input()
    if len(s) == 1:
        if int(s) % 8 == 0:
            print('Yes')
        else:
            print('No')
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        cnt = Counter(s)
        for i in range(112, 1000, 8):
            if not Counter(str(i)) - cnt:
                print('Yes')
                return
        print('No')
