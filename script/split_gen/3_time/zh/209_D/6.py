def main():
    n,q = map(int,raw_input().split())
    roads = []
    for i in range(n-1):
        a,b = map(int,raw_input().split())
        roads.append((a,b))
    for i in range(q):
        c,d = map(int,raw_input().split())
        if (c,d) in roads or (d,c) in roads:
            print "Road"
        else:
            print "Town"
