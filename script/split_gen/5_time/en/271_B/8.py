def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    L = []
    a = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        a.append(list(map(int, input().split())))
    #print(L)
    #print(a)
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])
