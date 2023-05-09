def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    ans = 10**9
    for i in range(n):
        if s[i] == 'R':
            r -= 1
        else:
            w -= 1
        ans = min(ans, r + w)
    print(ans)

if __name__ == '__main__':
    main()