def main():
    #read input
    n,m,q = map(int,input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int,input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int,input().split())))
    #solve problem
    for i in range(q):
        print(solve(trains,queries[i][0],queries[i][1]))
