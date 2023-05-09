def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            rev = not rev
        else:
            if (t[1] == '1') ^ rev:
                s.insert(0, t[2])
            else:
                s.append(t[2])
    if rev:
        s.reverse()
    print(''.join(s))

if __name__ == '__main__':
    main()