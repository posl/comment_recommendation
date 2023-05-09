def main():
    N,X = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int,input().split()))
        L.append(l[0])
        A.append(l[1:])
    #print(L)
    #print(A)
    #print(N,X)
    #print(len(L))
    #print(len(A))
    from itertools import product
    #print(list(product(*A)))
    #print(len(list(product(*A))))
    counter = 0
    for i in list(product(*A)):
        #print(i)
        if prod(i) == X:
            counter += 1
    print(counter)
    return
