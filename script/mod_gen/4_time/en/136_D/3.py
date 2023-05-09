def main():
    s = input()
    n = len(s)
    ans = [0 for _ in range(n)]
    r = 0
    l = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            l += 1
        if s[i] == 'R' and s[i+1] == 'L':
            ans[i+1] += r//2 + r%2
            ans[i] += r//2
            r = 0
        elif s[i] == 'L' and s[i+1] == 'R':
            ans[i-1] += l//2
            ans[i] += l//2 + l%2
            l = 0
    print(*ans)

if __name__ == '__main__':
    main()