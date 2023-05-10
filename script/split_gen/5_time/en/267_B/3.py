def main():
    s = input()
    if s[0] == '0':
        if s[1] == '1' and s[2] == '1':
            print('Yes')
        else:
            print('No')
    else:
        if s[1] == '0':
            if s[2] == '1' and s[3] == '1':
                print('Yes')
            else:
                print('No')
        else:
            if s[2] == '0':
                if s[3] == '1' and s[4] == '1':
                    print('Yes')
                else:
                    print('No')
            else:
                if s[3] == '0':
                    if s[4] == '1' and s[5] == '1':
                        print('Yes')
                    else:
                        print('No')
                else:
                    if s[4] == '0':
                        if s[5] == '1' and s[6] == '1':
                            print('Yes')
                        else:
                            print('No')
                    else:
                        if s[5] == '0':
                            if s[6] == '1' and s[7] == '1':
                                print('Yes')
                            else:
                                print('No')
                        else:
                            if s[6] == '0':
                                if s[7] == '1' and s[8] == '1':
                                    print('Yes')
                                else:
                                    print('No')
                            else:
                                if s[7] == '0':
                                    if s[8] == '1' and s[9] == '1':
                                        print('Yes')
                                    else:
                                        print('No')
                                else:
                                    if s[8] == '0':
                                        if s[9] == '1':
                                            print('Yes')
                                        else:
                                            print('No')
                                    else:
                                        print('No')
