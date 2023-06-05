def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    #print(query)
    c = 0
    for i in range(q):
        if query[i][0] == '1':
            c += int(query[i][2])
        else:
            print(c)
            c = 0
main()
