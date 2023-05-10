def main():
    # input
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(list(map(int, input().split())))
    # solve
    cylinder = []
    for query in queries:
        if query[0] == 1:
            cylinder += [query[1]] * query[2]
        elif query[0] == 2:
            print(sum(cylinder[:query[1]]))
            del cylinder[:query[1]]
    # output

if __name__ == '__main__':
    main()