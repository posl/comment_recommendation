def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        s = sorted(s)
        for i in range(100, 1000):
            if i % 8 == 0:
                j = str(i)
                j = sorted(j)
                if j[0] == '0':
                    continue
                else:
                    if j[0] == s[0] and j[1] == s[1] and j[2] == s[2]:
                        print('Yes')
                        break
        else:
            print('No')
