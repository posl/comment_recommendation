def main():
    n = int(input())
    s = input()
    ans = ''
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        if s[i] == ',' and cnt % 2 == 1:
            ans += '.'
        else:
            ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()