def main():
    S = input()
    Q = int(input())
    reverse = False
    head = []
    tail = []
    for i in range(Q):
        query = input()
        if query == '1':
            reverse = not reverse
        else:
            _, f, c = query.split()
            if f == '1':
                if reverse:
                    tail.append(c)
                else:
                    head.append(c)
            else:
                if reverse:
                    head.append(c)
                else:
                    tail.append(c)
    if reverse:
        print(''.join(tail[::-1]) + S[::-1] + ''.join(head))
    else:
        print(''.join(head[::-1]) + S + ''.join(tail))
