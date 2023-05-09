def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = []
    for i in range(N):
        B.append([A[i][0], A[i][1]])
        B.append([A[i][0]-1, A[i][1]])
        B.append([A[i][0], A[i][1]-1])
        B.append([A[i][0]+1, A[i][1]-1])
        B.append([A[i][0]-1, A[i][1]+1])
        B.append([A[i][0]+1, A[i][1]])
    B = set(map(tuple, B))
    B = list(B)
    B.sort()
    B = list(map(list, B))
    #print(B)
    #print(len(B))
    def union_find(n):
        par = [i for i in range(n)]
        rank = [0 for i in range(n)]
        def find(x):
            if par[x] == x:
                return x
            else:
                par[x] = find(par[x])
                return par[x]
        def same(x, y):
            return find(x) == find(y)
        def unite(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            elif rank[x] < rank[y]:
                par[x] = y
            else:
                par[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
            return True
        return find, same, unite
    find, same, unite = union_find(len(B))
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            if B[i][0] == B[j][0] and B[i][1] == B[j][1]+1:
                unite(i, j)
            if B[i][0] == B[j][0]+1 and B[i][1] == B[j][1]:
                unite(i, j)
            if B[i][0] == B[j][0]+1 and B[i][1] == B[j][1]+1:
                unite(i, j)
            if B[i][0] == B[j][0]+1 and B[i][1] == B[j][1]-1:
                unite(i, j

if __name__ == '__main__':
    main()