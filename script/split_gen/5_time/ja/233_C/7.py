def main():
    N,X = map(int,input().split())
    L = []
    a = []
    for i in range(N):
        L.append(list(map(int,input().split())))
        a.append(L[i][1:])
    #print(L)
    #print(a)
    #print(list(itertools.product(*a)))
    #print(list(itertools.chain.from_iterable(itertools.product(*a))))
    #print(list(itertools.chain.from_iterable(itertools.product(*a))))
    print(len([i for i in list(itertools.chain.from_iterable(itertools.product(*a))) if i == X]))
    #print(list(itertools.chain.from_iterable(itertools.product(*a))).count(X))
