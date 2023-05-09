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
    ans = min(r, w)
    if ans == 0:
        print(0)
        return
    r = 0
    w = 0
    for i in range(ans):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    print(ans - min(r, w))

if __name__ == '__main__':
    main()