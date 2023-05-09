def main():
    n, q = map(int, input().split())
    #print("n: ", n)
    #print("q: ", q)
    #parent[i]: parent of i
    #parent[i] = i: i is root
    parent = list(range(n+1))
    #print("parent: ", parent)
    #size[i]: size of tree whose root is i
    size = [1]*(n+1)
    #print("size: ", size)
    #rank[i]: rank of i
    #rank[i] = 0: i is root
    #rank[i] = k: i is a child of the root of rank k-1 tree
    rank = [0]*(n+1)
    #print("rank: ", rank)
    #car[i]: car number of i
    car = list(range(n+1))
    #print("car: ", car)
    #ans: list of queries of the format 3 x
    ans = []
    #print("ans: ", ans)
    #print("query: ")
    for i in range(q):
        query = list(map(int, input().split()))
        #print(query)
        if len(query) == 2:
            ans.append(query)
        else:
            query[1] = car[query[1]]
            query[2] = car[query[2]]
            unite(query[1], query[2], parent, size, rank)
    #print("ans: ", ans)
    #print("parent: ", parent)
    #print("size: ", size)
    #print("rank: ", rank)
    #print("car: ", car)
    for query in ans:
        #print("query: ", query)
        x = query[1]
        #print("x: ", x)
        #print("parent: ", parent)
        #print("car: ", car)
        #print("parent[car[x]]: ", parent[car[x]])
        #print("parent[car[x]]: ", parent[car[x]])
        #print("car[parent[car[x]]]: ", car[parent[car[x]]])
        #print("car[parent[car[x]]]: ", car[parent[car[x]]])
        while parent[car[x]] != car[x]:
            x = parent[car[x]]
        #print("x: ", x)
