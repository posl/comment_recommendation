def main():
    #入力
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a,b = map(int,input().split())
        S.append((a,b))
    for i in range(N):
        c,d = map(int,input().split())
        T.append((c,d))
    #print(S)
    #print(T)
    #処理
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            dx = S[0][0] - S[i][0]
            dy = S[0][1] - S[i][1]
            #print("dx,dy",dx,dy)
            S_tmp = []
            for k in range(N):
                a = S[k][0] + dx
                b = S[k][1] + dy
                S_tmp.append((a,b))
            #print("S_tmp",S_tmp)
            #print("T",T)
            if S_tmp == T:
                #print("Yes")
                print("Yes")
                return
    print("No")
    return
main()
