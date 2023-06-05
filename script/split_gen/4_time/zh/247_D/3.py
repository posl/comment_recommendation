def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    count = 0
    for i in range(Q):
        if query[i][0] == 1:
            count += query[i][1]*query[i][2]
        else:
            print(count)
            count = 0
