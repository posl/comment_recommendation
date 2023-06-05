def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    ans = min(r,w)
    for i in range(ans):
        if c[i] == 'W':
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()