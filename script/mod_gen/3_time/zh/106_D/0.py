def get_input():
    n,m,q = map(int,raw_input().split())
    trains = []
    for i in xrange(m):
        trains.append(map(int,raw_input().split()))
    queries = []
    for i in xrange(q):
        queries.append(map(int,raw_input().split()))
    return n,m,q,trains,queries

if __name__ == '__main__':
    get_input()