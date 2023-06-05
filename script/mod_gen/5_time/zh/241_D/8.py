def main():
    n = int(input())
    a = []
    for i in range(n):
        query = input()
        if query[0] == '1':
            a.append(int(query[2:]))
        elif query[0] == '2':
            x = int(query[2:query.find(' ', 2)])
            k = int(query[query.find(' ', 2)+1:])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[-k])
        else:
            x = int(query[2:query.find(' ', 2)])
            k = int(query[query.find(' ', 2)+1:])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[k-1])

if __name__ == '__main__':
    main()