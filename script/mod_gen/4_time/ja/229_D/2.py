def main():
    s = input()
    k = int(input())
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(min(ans+k, len(s)))

if __name__ == '__main__':
    main()