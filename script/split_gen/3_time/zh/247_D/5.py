def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(m) for m in input().split()])
    #print(query)
    cylinder = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                cylinder.append(query[i][1])
        if query[i][0] == 2:
            print(sum(cylinder[:query[i][1]]))
            cylinder = cylinder[query[i][1]:]
