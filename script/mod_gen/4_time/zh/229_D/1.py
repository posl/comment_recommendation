def main():
    s = input()
    k = int(input())
    cnt = 0
    max_cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    if k == 0:
        print(max_cnt)
        return
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            if i > 0 and s[i - 1] == 'X':
                cnt += 1
            if i < len(s) - 1 and s[i + 1] == 'X':
                cnt += 1
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    print(max_cnt)
    return

if __name__ == '__main__':
    main()