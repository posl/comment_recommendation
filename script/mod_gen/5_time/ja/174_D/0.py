def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    ans = min(r, w)
    rnum = 0
    wnum = 0
    for i in range(n):
        if s[i] == 'R':
            rnum += 1
        else:
            wnum += 1
        ans = min(ans, max(rnum, wnum))
    print(ans)

if __name__ == '__main__':
    main()