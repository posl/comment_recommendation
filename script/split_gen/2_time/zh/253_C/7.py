def main():
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    # print(queries)
    # print(q)
    s = []
    for i in range(q):
        if queries[i][0] == 1:
            s.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(min(queries[i][2], s.count(queries[i][1]))):
                s.remove(queries[i][1])
        elif queries[i][0] == 3:
            print(max(s) - min(s))
