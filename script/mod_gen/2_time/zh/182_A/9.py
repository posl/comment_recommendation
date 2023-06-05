def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('是')
        else:
            print('否')
        return
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    elif len(s) == 3:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 or int(s[1] + s[0] + s[2]) % 8 == 0 or int(s[1] + s[2] + s[0]) % 8 == 0 or int(s[2] + s[0] + s[1]) % 8 == 0 or int(s[2] + s[1] + s[0]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    else:
        d = [0] * 10
        for i in range(len(s)):
            d[int(s[i])] += 1
        for i in range(112, 1000, 8):
            t = i
            dt = [0] * 10
            for j in range(3):
                dt[t % 10] += 1
                t //= 10
            flag = True
            for j in range(10):
                if dt[j] > d[j]:
                    flag = False
                    break
            if flag:
                print('是')
                return
        print('否')
        return

if __name__ == '__main__':
    main()