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
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 or int(s[1] + s[2] + s[0]) % 8 == 0 or int(s[1] + s[0] + s[2]) % 8 == 0 or int(s[2] + s[0] + s[1]) % 8 == 0 or int(s[2] + s[1] + s[0]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    elif len(s) >= 4:
        num = [0] * 10
        for i in s:
            num[int(i)] += 1
        for i in range(1000, 10000):
            if i % 8 != 0:
                continue
            tmp = [0] * 10
            tmp[i % 10] += 1
            tmp[i // 10 % 10] += 1
            tmp[i // 100 % 10] += 1
            tmp[i // 1000 % 10] += 1
            if tmp[0] > 0:
                continue
            flag = True
            for j in range(1, 10):
                if num[j] < tmp[j]:
                    flag = False
                    break
            if flag:
                print('是')
                return
        print('否')
        return
