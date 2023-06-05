def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input().split())
    result = []
    bag = []
    for query in queries:
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for i in range(len(bag)):
                bag[i] += int(query[1])
        else:
            min_num = min(bag)
            result.append(min_num)
            bag.remove(min_num)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()