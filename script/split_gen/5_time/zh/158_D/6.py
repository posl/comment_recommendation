def main():
    s = input().strip()
    q = int(input().strip())
    reverse = False
    head = ''
    tail = ''
    for _ in range(q):
        query = input().strip().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            f = query[1]
            c = query[2]
            if f == '1':
                if reverse:
                    tail += c
                else:
                    head += c
            else:
                if reverse:
                    head += c
                else:
                    tail += c
    res = head + s + tail
    if reverse:
        res = res[::-1]
    print(res)
