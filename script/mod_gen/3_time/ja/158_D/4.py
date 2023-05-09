def main():
    S = input()
    Q = int(input())
    S = list(S)
    reverse = False
    for i in range(Q):
        query = input()
        if query == '1':
            reverse = not reverse
        else:
            query = query.split()
            if query[1] == '1':
                if reverse:
                    S.append(query[2])
                else:
                    S.insert(0, query[2])
            else:
                if reverse:
                    S.insert(0, query[2])
                else:
                    S.append(query[2])
    if reverse:
        S = S[::-1]
    print(''.join(S))

if __name__ == '__main__':
    main()