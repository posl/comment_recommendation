def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    cnt = 1
    max = 0
    ans = []
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            if max < cnt:
                max = cnt
                ans = []
                ans.append(s[i-1])
            elif max == cnt:
                ans.append(s[i-1])
            cnt = 1
    if max < cnt:
        max = cnt
        ans = []
        ans.append(s[n-1])
    elif max == cnt:
        ans.append(s[n-1])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()