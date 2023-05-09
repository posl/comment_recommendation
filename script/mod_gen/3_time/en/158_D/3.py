def main():
    s = input()
    q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            rev = not rev
        else:
            if query[1] == '1':
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
        head.reverse()
        head = ''.join(head)
        s = s[::-1]
        print(head + s + ''.join(tail))
    else:
        tail.reverse()
        tail = ''.join(tail)
        print(tail + s + ''.join(head))

if __name__ == '__main__':
    main()