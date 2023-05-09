def main():
    N,Q = map(int,input().split())
    train = [i+1 for i in range(N)]
    train.insert(0,0)
    train.append(0)
    #print(train)
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            train[query[2]] = train[query[1]]
        elif query[0] == 2:
            train[query[1]] = query[2]
        elif query[0] == 3:
            ans = []
            ans.append(query[1])
            while train[query[1]] != 0:
                ans.append(train[query[1]])
                query[1] = train[query[1]]
            print(len(ans),*ans)
