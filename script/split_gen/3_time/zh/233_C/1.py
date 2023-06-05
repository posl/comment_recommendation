def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(N, X, L)
    #print(L[0][1])
    ans = 0
    for i in range(N):
        for j in range(L[i][0]):
            #print(L[i][j+1])
            if X % L[i][j+1] == 0:
                #print("yes")
                for k in range(N):
                    for l in range(L[k][0]):
                        #print(L[k][l+1])
                        if X / L[i][j+1] == L[k][l+1]:
                            ans += 1
    print(ans)
