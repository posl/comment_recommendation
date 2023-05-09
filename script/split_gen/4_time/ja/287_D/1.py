def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(lt):
        if s[i] == '?':
            continue
        elif s[i] != t[i]:
            print('No')
            exit()
    for i in range(lt,ls):
        if s[i] == '?':
            continue
        elif s[i] != t[i-lt]:
            print('No')
            exit()
    print('Yes')
