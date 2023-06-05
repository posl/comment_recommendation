def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == 'R':
            if i+1 < n and s[i+1] == 'R':
                ans[i+2] += ans[i]
                ans[i] = 0
            else:
                ans[i+1] += ans[i] + 1
                ans[i] = 0
        else:
            ans[i-1] += ans[i]
            ans[i] = 0
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()