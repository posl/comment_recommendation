def main():
    S = input()
    Q = int(input())
    rev = False
    head = ""
    tail = ""
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            rev = not rev
        else:
            if (query[1] == "1" and not rev) or (query[1] == "2" and rev):
                head += query[2]
            else:
                tail += query[2]
    if rev:
        print(tail[::-1] + S[::-1] + head)
    else:
        print(head[::-1] + S + tail)

if __name__ == '__main__':
    main()