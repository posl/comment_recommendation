def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('是')
        else:
            print('否')
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    if len(s) >= 3:
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for i in range(104, 1000, 8):
            i_dict = {}
            for j in str(i):
                if j in i_dict:
                    i_dict[j] += 1
                else:
                    i_dict[j] = 1
            flag = True
            for k in i_dict:
                if k not in s_dict or i_dict[k] > s_dict[k]:
                    flag = False
                    break
            if flag:
                print('是')
                return
        print('否')
        return

if __name__ == '__main__':
    main()