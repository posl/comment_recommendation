def main():
    N = int(input())
    query = []
    result = []
    for i in range(N):
        query.append(list(map(int, input().split())))
    bag = []
    for i in range(N):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        elif query[i][0] == 3:
            result.append(min(bag))
            bag.remove(min(bag))
    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    main()