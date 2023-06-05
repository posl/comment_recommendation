def main():
    L,Q = map(int,input().split())
    #print(L,Q)
    cut = []
    for i in range(Q):
        cut.append(list(map(int,input().split())))
        #print(cut[i])
    #print(cut)
    cut.sort(key = lambda x:x[1])
    #print(cut)
    #print(cut[0][1])
    #print(cut[1][1])
    #print(cut[2][1])
    #print(cut[3][1])
    #print(cut[4][1])
    #print(cut[5][1])
    #print(cut[6][1])
    #print(cut[7][1])
    #print(cut[8][1])
    #print(cut[9][1])
    ans = []
    for i in range(Q):
        if cut[i][0] == 1:
            cut.append([1,cut[i][1]])
            cut.append([1,L-cut[i][1]])
        else:
            #print(cut)
            #print(cut[i][1])
            #print(cut[i][1]-cut[i-1][1])
            #print(cut[i][1]-cut[i-1][1])
            ans.append(cut[i][1]-cut[i-1][1])
    for i in range(len(ans)):
        print(ans[i])
