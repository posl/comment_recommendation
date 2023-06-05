def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    cur = 0
    for i in range(n):
        if s[i] == 'X':
            cur += 1
        else:
            if k > 0:
                k -= 1
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 0
    ans = max(ans, cur)
    print(ans)

if __name__ == '__main__':
    main()