def main():
    s = input()
    k = int(input())
    if k == 0:
        print(len(max(s.split('.'), key=len)))
        return
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            if cnt >= k:
                break
            cnt = 0
    print(cnt + k)

if __name__ == '__main__':
    main()