def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == '1':
            rev = not rev
        else:
            if t[1] == '1':
                if rev:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
            else:
                if rev:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
    if rev:
        s = s[::-1]
    print("".join(s))

if __name__ == '__main__':
    main()