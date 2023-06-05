def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ABC = []
    for a in A:
        for b in B:
            ABC.append(a+b)
    ABC.sort(reverse=True)
    ABC = ABC[:K]
    ABCD = []
    for c in C:
        for abc in ABC:
            ABCD.append(c+abc)
    ABCD.sort(reverse=True)
    for i in range(K):
        print(ABCD[i])
