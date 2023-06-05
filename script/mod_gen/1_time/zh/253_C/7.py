def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    S = []
    for i in range(q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            x = query[i][1]
            c = query[i][2]
            count = 0
            for j in range(len(S)):
                if S[j] == x:
                    count += 1
                    if count == c:
                        S.pop(j)
                        break
        elif query[i][0] == 3:
            print(max(S) - min(S))

if __name__ == '__main__':
    main()