def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    #print(query)
    s = []
    for i in range(q):
        if query[i][0] == '1':
            s.append(int(query[i][1]))
        elif query[i][0] == '2':
            for j in range(int(query[i][2])):
                if int(query[i][1]) in s:
                    s.remove(int(query[i][1]))
                else:
                    break
        else:
            print(max(s) - min(s))
    #print(s)

if __name__ == '__main__':
    main()