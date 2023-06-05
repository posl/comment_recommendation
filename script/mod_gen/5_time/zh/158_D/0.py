def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input().split()
        if len(t) == 1:
            s = s[::-1]
        else:
            f = int(t[1])
            c = t[2]
            if f == 1:
                s = c + s
            else:
                s = s + c
    print(s)

if __name__ == '__main__':
    main()