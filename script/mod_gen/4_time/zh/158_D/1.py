def main():
    s = input()
    q = int(input())
    t = 0
    f = 0
    c = ''
    for i in range(q):
        t, f, c = input().split()
        t = int(t)
        f = int(f)
        if t == 1:
            s = s[::-1]
        else:
            if f == 1:
                s = c + s
            else:
                s = s + c
    print(s)

if __name__ == '__main__':
    main()