def main():
    s = input()
    q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            rev = not rev
        else:
            if query[1] == "1":
                if rev:
                    tail.append(query[2])
                else:
                    head.append(query[2])
            else:
                if rev:
                    head.append(query[2])
                else:
                    tail.append(query[2])
    if rev:
        print("".join(tail[::-1]) + s[::-1] + "".join(head[::-1]))
    else:
        print("".join(head) + s + "".join(tail))

if __name__ == '__main__':
    main()