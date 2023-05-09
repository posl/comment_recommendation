def main():
    n,q = map(int,input().split())
    trains = [i for i in range(n)]
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x,y = query[1],query[2]
            if x == y:
                continue
            if trains[x-1] == trains[y-1]:
                continue
            else:
                trains = [trains[x-1] if i == trains[y-1] else i for i in trains]
        elif query[0] == 2:
            x,y = query[1],query[2]
            if x == y:
                continue
            if trains[x-1] != trains[y-1]:
                continue
            else:
                trains = [i if i != trains[x-1] else i+1 for i in trains]
        elif query[0] == 3:
            x = query[1]
            ans = [i+1 for i in range(n) if trains[i] == trains[x-1]]
            print(len(ans),*ans)
