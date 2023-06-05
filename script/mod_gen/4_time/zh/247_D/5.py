def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    cylinder = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                cylinder.append(query[i][1])
        else:
            print(sum(cylinder[:query[i][1]]))
            cylinder = cylinder[query[i][1]:]

if __name__ == '__main__':
    main()