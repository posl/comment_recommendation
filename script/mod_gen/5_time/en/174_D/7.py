def main():
    n = int(input())
    c = input()
    w = c.count('W')
    r = c.count('R')
    ans = min(w, r)
    w = 0
    r = 0
    for i in range(n):
        if c[i] == 'W':
            w += 1
        else:
            r += 1
        ans = min(ans, max(w, r))
    print(ans)

if __name__ == '__main__':
    main()