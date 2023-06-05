def main():
    n = int(input())
    query = []
    for i in range(n):
        query.append(list(map(int, input().split())))
    query.reverse()
    bag = []
    for i in range(n):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        elif query[i][0] == 3:
            print(bag.pop(bag.index(min(bag))))

if __name__ == '__main__':
    main()