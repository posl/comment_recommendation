def main():
    N,Q = list(map(int,input().split()))
    train = [i for i in range(N+1)]
    #print(train)
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            #print("query[0] == 1")
            x = train[query[1]]
            y = train[query[2]]
            #print("x = train[query[1]]",x)
            #print("y = train[query[2]]",y)
            train[x] = y
            #print("train[x] = y",train[x])
        elif query[0] == 2:
            #print("query[0] == 2")
            x = train[query[1]]
            y = train[query[2]]
            #print("x = train[query[1]]",x)
            #print("y = train[query[2]]",y)
            train[x] = x
            #print("train[x] = x",train[x])
        else:
            #print("query[0] == 3")
            x = train[query[1]]
            #print("x = train[query[1]]",x)
            ans = [query[1]]
            while x != train[x]:
                ans.append(train[x])
                x = train[x]
            print(len(ans),*ans)
            #print("len(ans),*ans",len(ans),*ans)
    return
