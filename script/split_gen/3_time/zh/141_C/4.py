def get_input():
    n,k,q = map(int,input().split())
    alist = []
    for i in range(q):
        alist.append(int(input()))
    return n,k,q,alist
