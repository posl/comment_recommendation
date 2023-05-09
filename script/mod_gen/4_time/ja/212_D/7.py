def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    #print(query)
    bag = []
    for i in range(Q):
        #print("query[i][0] = ", query[i][0])
        #print("query[i][1] = ", query[i][1])
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        elif query[i][0] == 3:
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()