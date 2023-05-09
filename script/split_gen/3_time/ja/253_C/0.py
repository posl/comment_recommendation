def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    S = []
    for i in range(Q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(query[i][1]):
                if query[i][2] > 0:
                    if query[i][2] > S.count(query[i][1]):
                        S.remove(query[i][1])
                        query[i][2] -= 1
                    else:
                        break
        elif query[i][0] == 3:
            print(max(S) - min(S))
