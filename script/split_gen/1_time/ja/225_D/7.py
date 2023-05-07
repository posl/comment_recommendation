def main():
    import sys
    input = sys.stdin.readline
    #入力
    N,Q = map(int,input().split())
    train = [0]*N
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            train[query[2]-1] = query[1]
        elif query[0] == 2:
            train[query[2]-1] = 0
        else:
            ans = []
            ans.append(query[1])
            while train[ans[-1]-1] != 0:
                ans.append(train[ans[-1]-1])
            print(len(ans),*ans)
