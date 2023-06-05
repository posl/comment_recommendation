def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    r = []
    for i in query:
        if i[0] == 1:
            r.append(i[1] * i[2])
        else:
            print(sum(r[:i[1]]))
main()
