def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    ans = min(r, w)
    for i in range(ans):
        if s[i] == 'R':
            r -= 1
    ans += r
    print(ans)

if __name__ == '__main__':
    main()