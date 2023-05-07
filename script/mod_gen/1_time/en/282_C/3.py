def main():
    n = int(input())
    s = input()
    ans = ""
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        if count % 2 == 0:
            if s[i] == ',':
                ans += '.'
            else:
                ans += s[i]
        else:
            ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()