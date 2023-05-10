def main():
    l,q = map(int,input().split())
    cuts = set([0,l])
    for i in range(q):
        c,x = map(int,input().split())
        if c == 1:
            cuts.add(x)
        else:
            print(max(cuts) - min(cuts))
