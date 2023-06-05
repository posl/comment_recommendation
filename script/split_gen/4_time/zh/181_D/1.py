def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('是')
        else:
            print('否')
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print('是')
        else:
            print('否')
    else:
        s = list(s)
        for i in range(len(s)):
            if int(s[i]) % 2 == 1:
                s[i] = '0'
        s = ''.join(s)
        s = s.replace('0', '')
        s = list(s)
        if len(s) == 0:
            print('否')
        elif len(s) == 1:
            if s == '8':
                print('是')
            else:
                print('否')
        elif len(s) == 2:
            if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
                print('是')
            else:
                print('否')
        else:
            s = list(s)
            for i in range(len(s)):
                if int(s[i]) % 2 == 1:
                    s[i] = '0'
            s = ''.join(s)
            s = s.replace('0', '')
            s = list(s)
            if len(s) == 0:
                print('否')
            elif len(s) == 1:
                if s == '8':
                    print('是')
                else:
                    print('否')
            elif len(s) == 2:
                if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
                    print('是')
                else:
                    print('否')
            else:
                s = list(s)
                for i in range(len(s)):
                    if int(s[i]) % 2 == 1:
                        s[i] = '0'
                s = ''.join(s)
                s = s.replace('0', '')
                s = list(s)
                if len(s) == 0:
                    print('否')
                elif len(s) == 1:
                    if s == '8':
                        print('是')
                    else:
                        print('否')
                elif
