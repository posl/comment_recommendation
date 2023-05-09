def main():
    import sys
    #f = open('test.txt','r')
    f = sys.stdin
    n,m,q = map(int,f.readline().split())
    trains = [list(map(int,f.readline().split())) for i in range(m)]
    queries = [list(map(int,f.readline().split())) for i in range(q)]
    #print(n,m,q)
    #print(trains)
    #print(queries)
    for query in queries:
        count = 0
        for train in trains:
            if train[0] >= query[0] and train[1] <= query[1]:
                count += 1
        print(count)
