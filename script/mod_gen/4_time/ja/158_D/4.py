def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        query = input().split()
        t = int(query[0])
        if t == 1:
            rev = not rev
        else:
            f = int(query[1])
            c = query[2]
            if f == 1:
                if rev:
                    s.append(c)
                else:
                    s.insert(0, c)
            else:
                if rev:
                    s.insert(0, c)
                else:
                    s.append(c)
    if rev:
        s.reverse()
    print("".join(s))

if __name__ == '__main__':
    main()