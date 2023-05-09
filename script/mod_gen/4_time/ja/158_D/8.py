def main():
    s = input()
    q = int(input())
    s = list(s)
    head = []
    tail = []
    reverse = False
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        else:
            if query[1] == "1":
                if reverse:
                    tail.append(query[2])
                else:
                    head.append(query[2])
            else:
                if reverse:
                    head.append(query[2])
                else:
                    tail.append(query[2])
    if reverse:
        s = s[::-1]
        tail = tail[::-1]
        head = head[::-1]
    ans = "".join(head) + "".join(s) + "".join(tail)
    print(ans)

if __name__ == '__main__':
    main()