def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(input().split())
    bag = []
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]))
        elif query[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[i][1])
        else:
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()