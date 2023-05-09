def main():
    s = input()
    q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(q):
        t = list(input().split())
        if t[0] == "1":
            rev = not rev
        else:
            if t[1] == "1":
                if rev:
                    tail.append(t[2])
                else:
                    head.append(t[2])
            else:
                if rev:
                    head.append(t[2])
                else:
                    tail.append(t[2])
    if rev:
        print("".join(tail[::-1]) + s[::-1] + "".join(head))
    else:
        print("".join(head[::-1]) + s + "".join(tail))

if __name__ == '__main__':
    main()