def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('是')
        else:
            print('否')
    elif len(s) == 2:
        if s == '16' or s == '24' or s == '32' or s == '48' or s == '56' or s == '64' or s == '72' or s == '88':
            print('是')
        else:
            print('否')
    else:
        if s.find('8') == -1:
            print('否')
        else:
            s = s.replace('8', '')
            if len(s) == 0:
                print('是')
            else:
                if len(s) == 1:
                    if s == '8':
                        print('是')
                    else:
                        print('否')
                elif len(s) == 2:
                    if s == '16' or s == '24' or s == '32' or s == '48' or s == '56' or s == '64' or s == '72' or s == '88':
                        print('是')
                    else:
                        print('否')
                else:
                    if s.find('8') == -1:
                        print('否')
                    else:
                        s = s.replace('8', '')
                        if len(s) == 0:
                            print('是')
                        else:
                            if len(s) == 1:
                                if s == '8':
                                    print('是')
                                else:
                                    print('否')
                            elif len(s) == 2:
                                if s == '16' or s == '24' or s == '32' or s == '48' or s == '56' or s == '64' or s == '72' or s == '88':
                                    print('是')
                                else:
                                    print('否')
                            else:
                                if s.find('8') == -1:
                                    print('否')
                                else:
                                    s = s.replace('8', '')
                                    if len(s) == 0:
                                        print('是')
                                    else:
                                        if len(s) == 1:
                                            if s == '8':
                                                print('是')
                                            else:
                                                print('否')
                                        elif len(s) == 2:
                                            if s == '16' or s == '
