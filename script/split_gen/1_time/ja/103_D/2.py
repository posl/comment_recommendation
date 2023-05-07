def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    #print(N, M)
    #print(AB)
    #print(AB[0][1])
    #print(AB[1][1])
    #print(AB[2][1])
    #print(AB[3][1])
    #print(AB[4][1])
    #print(AB[5][1])
    #print(AB[6][1])
    #print(AB[7][1])
    #print(AB[8][1])
    #print(AB[9][1])
    #print(AB[10][1])
    ans = 0
    #print(AB)
    #print(AB[0][0])
    #print(AB[1][0])
    #print(AB[2][0])
    #print(AB[3][0])
    #print(AB[4][0])
    #print(AB[5][0])
    #print(AB[6][0])
    #print(AB[7][0])
    #print(AB[8][0])
    #print(AB[9][0])
    #print(AB[10][0])
    for i in range(M):
        #print(AB[i][0])
        #print(AB[i][1])
        if AB[i][0] == AB[i][1]:
            ans += 1
        elif AB[i][0] < AB[i][1]:
            AB[i][0] += 1
            #print(AB[i][0])
            #print(AB[i][1])
            #print(AB)
            #print(AB[0][0])
            #print(AB[1][0])
            #print(AB[2][0])
            #print(AB[3][0])
            #print(AB[4][0])
            #print(AB[5][0])
            #print(AB[6][0])
            #print(AB[7][0])
            #print(AB[8][0])
            #print(AB[9][0])
            #print(
