def main():
    s = input()
    n = len(s)
    ans = [0]*n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
        if l > 0 and r > 0:
            if s[i] == 'R':
                ans[i] += l//2
                ans[i-1] += l - l//2
                l = 0
            else:
                ans[i] += r//2
                ans[i-1] += r - r//2
                r = 0
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()