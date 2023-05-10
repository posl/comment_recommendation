def main():
    import sys
    sys.setrecursionlimit(10 ** 7)
    input = sys.stdin.readline
    s = input().strip()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        cnt = [0] * 10
        for i in range(len(s)):
            cnt[int(s[i])] += 1
        for i in range(112, 1000, 8):
            tmp = [0] * 10
            tmp[i // 100] += 1
            tmp[i // 10 % 10] += 1
            tmp[i % 10] += 1
            ok = True
            for j in range(10):
                if cnt[j] < tmp[j]:
                    ok = False
            if ok:
                print('Yes')
                exit()
        print('No')

if __name__ == '__main__':
    main()