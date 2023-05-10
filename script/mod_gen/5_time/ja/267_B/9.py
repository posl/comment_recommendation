def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    if s[9] == '0':
        print('No')
        return
    if s[1:3] == '00' and s[6:9] == '000':
        print('Yes')
        return
    if s[1:3] == '00' and s[6:9] == '000':
        print('Yes')
        return
    if s[1:4] == '000' and s[7:9] == '00':
        print('Yes')
        return
    if s[1:5] == '0000' and s[8:9] == '0':
        print('Yes')
        return
    if s[1:6] == '00000' and s[9:9] == '':
        print('Yes')
        return
    if s[2:4] == '00' and s[5:8] == '000':
        print('Yes')
        return
    if s[2:5] == '000' and s[6:8] == '00':
        print('Yes')
        return
    if s[2:6] == '0000' and s[7:8] == '0':
        print('Yes')
        return
    if s[2:7] == '00000' and s[8:8] == '':
        print('Yes')
        return
    if s[3:5] == '00' and s[4:7] == '000':
        print('Yes')
        return
    if s[3:6] == '000' and s[5:7] == '00':
        print('Yes')
        return
    if s[3:7] == '0000' and s[6:7] == '0':
        print('Yes')
        return
    if s[3:8] == '00000' and s[7:7] == '':
        print('Yes')
        return
    if s[4:6] == '00' and s[3:6] == '000':
        print('Yes')
        return
    if s[4:7] == '000' and s[4:6] == '00':

if __name__ == '__main__':
    main()