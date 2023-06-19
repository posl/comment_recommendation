def solve():
    s = input().split()
    t = input().split()
    for i in range(3):
        if s[i] == t[i]:
            continue
        else:
            print('No')
            return
    print('Yes')
    return
