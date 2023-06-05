def main():
    s = input()
    q = int(input())
    reverse = False
    head = ''
    tail = ''
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    tail += query[2]
                else:
                    head += query[2]
            else:
                if reverse:
                    head += query[2]
                else:
                    tail += query[2]
    if reverse:
        head, tail = tail[::-1], head[::-1]
    print(head + s + tail)

if __name__ == '__main__':
    main()