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
    r_ = 0
    w_ = 0
    for i in range(N):
        if c[i] == 'R':
            r_ += 1
        else:
            w_ += 1
        if r_ == r and w_ == w:
            print(i + 1)
            return
    print(r)

if __name__ == '__main__':
    main()