def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    ans = min(r, w)
    for i in range(r):
        if c[i] == 'R':
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()