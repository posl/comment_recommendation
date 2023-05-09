def main():
    s = list(input())
    q = int(input())
    reverse = False
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    s.append(query[2])
                else:
                    s.insert(0, query[2])
            else:
                if reverse:
                    s.insert(0, query[2])
                else:
                    s.append(query[2])
    if reverse:
        s.reverse()
    print(''.join(s))

if __name__ == '__main__':
    main()