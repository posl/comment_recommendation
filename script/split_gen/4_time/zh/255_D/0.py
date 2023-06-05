def get_input():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    return n,q,a,x
