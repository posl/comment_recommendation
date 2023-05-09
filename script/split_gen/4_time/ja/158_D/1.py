def main():
    s = input()
    q = int(input())
    rev = False
    head = ''
    tail = ''
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            rev = not rev
        else:
            if query[1] == '1':
                if rev:
                    tail += query[2]
                else:
                    head += query[2]
            else:
                if rev:
                    head += query[2]
                else:
                    tail += query[2]
    if rev:
        s = s[::-1]
        head = head[::-1]
        tail = tail[::-1]
    print(head + s + tail)
