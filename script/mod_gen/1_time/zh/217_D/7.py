def readinput():
    L,Q = map(int,input().split())
    queries = []
    for _ in range(Q):
        c,x = map(int,input().split())
        queries.append((c,x))
    return (L,Q,queries)

if __name__ == '__main__':
    readinput()