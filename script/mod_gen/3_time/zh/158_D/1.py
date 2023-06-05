def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    reverse = False
    for i in range(q):
        if query[i][0] == '1':
            reverse = not reverse
        elif query[i][0] == '2':
            if query[i][1] == '1':
                if reverse:
                    s += query[i][2]
                else:
                    s = query[i][2] + s
            elif query[i][1] == '2':
                if reverse:
                    s = s + query[i][2]
                else:
                    s = query[i][2] + s
    if reverse:
        s = s[::-1]
    print(s)

if __name__ == '__main__':
    main()