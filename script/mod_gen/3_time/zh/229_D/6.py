def main():
    s = input()
    k = int(input())
    n = len(s)
    cnt = 0
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            cnt += 1
        else:
            if k > 0:
                k -= 1
                cnt += 1
            else:
                cnt = 0
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()