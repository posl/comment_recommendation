def main():
    S = input()
    Q = int(input())
    rev = 0
    head = []
    tail = []
    for i in range(Q):
        query = input().split()
        if len(query) == 1:
            rev ^= 1
        else:
            if query[1] == "1":
                if rev == 0:
                    head.append(query[2])
                else:
                    tail.append(query[2])
            else:
                if rev == 0:
                    tail.append(query[2])
                else:
                    head.append(query[2])
    if rev == 0:
        head.reverse()
        print("".join(head) + S + "".join(tail))
    else:
        tail.reverse()
        print("".join(tail)[::-1] + S[::-1] + "".join(head)[::-1])

if __name__ == '__main__':
    main()