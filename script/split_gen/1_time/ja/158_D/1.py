def main():
    S = input()
    Q = int(input())
    rev = False
    head = []
    tail = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            rev = not rev
        else:
            if query[1] == "1":
                if not rev:
                    head.append(query[2])
                else:
                    tail.append(query[2])
            else:
                if not rev:
                    tail.append(query[2])
                else:
                    head.append(query[2])
    if rev:
        head, tail = tail, head
    print("".join(head[::-1]) + S + "".join(tail))
