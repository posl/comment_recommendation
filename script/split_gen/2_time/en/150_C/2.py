def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    P = [x - 1 for x in P]
    Q = [x - 1 for x in Q]
    #print(P)
    #print(Q)
    P = tuple(P)
    Q = tuple(Q)
    #print(P)
    #print(Q)
    #print(type(P))
    #print(type(Q))
    X = list(range(N))
    X = tuple(X)
    #print(X)
    #print(type(X))
    import itertools
    a = 0
    b = 0
    for i, x in enumerate(itertools.permutations(X)):
        if x == P:
            a = i
        if x == Q:
            b = i
    print(abs(a - b))
