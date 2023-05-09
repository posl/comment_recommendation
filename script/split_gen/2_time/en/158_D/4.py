def main():
    S = input()
    Q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(Q):
        query = list(input().split())
        if query[0] == '1':
            rev = not rev
        else:
            if (query[1] == '1' and not rev) or (query[1] == '2' and rev):
                head.append(query[2])
            else:
                tail.append(query[2])
    head = ''.join(head)
    tail = ''.join(tail)
    if rev:
        print(tail[::-1] + S[::-1] + head[::-1])
    else:
        print(head + S + tail)
