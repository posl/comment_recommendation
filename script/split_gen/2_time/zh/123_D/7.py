def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ab = []
    for aa in a:
        for bb in b:
            ab.append(aa+bb)
    ab.sort(reverse=True)
    abc = []
    for i in range(k):
        for cc in c:
            abc.append(ab[i]+cc)
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])
