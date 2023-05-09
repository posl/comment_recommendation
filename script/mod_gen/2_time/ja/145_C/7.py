def main():
    import math
    import itertools
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    #print(XY)
    L = []
    for i in range(N):
        for j in range(i+1, N):
            L.append(math.sqrt((XY[i][0] - XY[j][0])**2 + (XY[i][1] - XY[j][1])**2))
    #print(L)
    A = list(itertools.permutations(L, len(L)))
    #print(A)
    B = []
    for i in range(len(A)):
        B.append(sum(A[i]))
    #print(B)
    print(sum(B)/len(B))

if __name__ == '__main__':
    main()