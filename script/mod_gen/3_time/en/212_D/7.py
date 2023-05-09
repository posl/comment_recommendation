def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input().split())
    #print(queries)
    bag = []
    for i in range(Q):
        if queries[i][0] == '1':
            bag.append(int(queries[i][1]))
        elif queries[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(queries[i][1])
        elif queries[i][0] == '3':
            print(min(bag))
            bag.remove(min(bag))
        #print(bag)
        
    return

if __name__ == '__main__':
    main()