def solve():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(ls-lt+1):
        flag = True
        for j in range(lt):
            if s[i+j] != t[j] and s[i+j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
    for i in range(ls-lt+1,lt+1):
        print('No')
