def main():
    Q = int(input())
    # query = []
    # for i in range(Q):
    #     query.append(list(map(int, input().split())))
    query = [list(map(int, input().split())) for i in range(Q)]
    # print(query)
    ans = []
    for i in range(Q):
        if query[i][0] == 1:
            ans.append(query[i][1] * query[i][2])
        else:
            ans.append(sum(ans[:query[i][1]]))
    # print(ans)
    for i in ans:
        print(i)
