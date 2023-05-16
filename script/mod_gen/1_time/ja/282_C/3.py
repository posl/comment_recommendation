def main():
    n = int(input())
    s = input()
    ans = ""
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 0:
            ans += '.'
        else:
            ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()