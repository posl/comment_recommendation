def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        print(a[query[i][0]-1:query[i][1]].count(query[i][2]))
