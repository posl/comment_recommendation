def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    #print(a)
    #print(query)
    #print(n, q)
    #print(a)
    #print(query)
    for i in range(q):
        if query[i][0] == 1:
            a = [query[i][1]]*n
        if query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        if query[i][0] == 3:
            print(a[query[i][1]-1])
