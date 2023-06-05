def main():
    s = input()
    n = len(s)
    if n == 1:
        if s == '8':
            print('是')
        else:
            print('否')
        return
    
    if n == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    
    if n >= 3:
        cnt = [0] * 10
        for c in s:
            cnt[int(c)] += 1
        for i in range(112, 1000, 8):
            d = [0] * 10
            d[i // 100] += 1
            d[i // 10 % 10] += 1
            d[i % 10] += 1
            flag = True
            for j in range(10):
                if cnt[j] < d[j]:
                    flag = False
                    break
            if flag:
                print('是')
                return
        print('否')
        return
