def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    S = [list(s) for s in S]
    T = [list(t) for t in T]
    #print(S)
    #print(T)
    #T の # の位置を取得
    t_pos = []
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                t_pos.append([i,j])
    #print(t_pos)
    #S の # の位置を取得
    s_pos = []
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                s_pos.append([i,j])
    #print(s_pos)
    #S の # の位置を移動させて、T の # の位置と一致させる
    for i in range(N):
        for j in range(N):
            #print(i,j)
            #print(s_pos)
            #print(t_pos)
            flag = True
            for k in range(len(s_pos)):
                #print(s_pos[k],t_pos[k])
                if s_pos[k][0] + i == t_pos[k][0] and s_pos[k][1] + j == t_pos[k][1]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()