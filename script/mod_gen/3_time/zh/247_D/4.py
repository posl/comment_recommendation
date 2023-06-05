def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    #print(query)
    balls = []
    for i in range(q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                balls.append(query[i][1])
        elif query[i][0] == 2:
            print(sum(balls[:query[i][1]]))

if __name__ == '__main__':
    main()