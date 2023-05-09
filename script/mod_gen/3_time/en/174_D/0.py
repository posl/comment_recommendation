def main():
    N = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        return
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
        if i < r:
            r = i + 1
        if i < w:
            w = i + 1
    print(min(r,w))

if __name__ == '__main__':
    main()