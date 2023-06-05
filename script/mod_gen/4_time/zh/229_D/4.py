def main():
    s = input()
    k = int(input())
    l = len(s)
    i = 0
    j = 0
    ans = 0
    while i < l:
        if s[i] == 'X':
            j += 1
            i += 1
        else:
            if k > 0:
                ans = max(ans, j + 1)
                k -= 1
                i += 1
                j += 1
            else:
                ans = max(ans, j)
                j = 0
                i += 1
    ans = max(ans, j)
    print(ans)

if __name__ == '__main__':
    main()