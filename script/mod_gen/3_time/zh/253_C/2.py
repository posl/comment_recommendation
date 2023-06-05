def main():
    Q = int(input())
    # query_list = []
    # for i in range(Q):
    #     query = input()
    #     query_list.append(query)
    query_list = [input() for i in range(Q)]
    query_list = [query.split() for query in query_list]
    query_list = [[int(query[0]), query[1:]] for query in query_list]
    S = []
    for query in query_list:
        if query[0] == 1:
            S.append(int(query[1][0]))
        elif query[0] == 2:
            x, c = int(query[1][0]), int(query[1][1])
            for i in range(c):
                if x in S:
                    S.remove(x)
                else:
                    break
        elif query[0] == 3:
            print(max(S) - min(S))

if __name__ == '__main__':
    main()