def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int,input().split())))
    for i in range(N):
        T.append(list(map(int,input().split())))
    #S,Tの中心を原点に移動
    S_center = [0,0]
    T_center = [0,0]
    for i in range(N):
        S_center[0] += S[i][0]
        S_center[1] += S[i][1]
        T_center[0] += T[i][0]
        T_center[1] += T[i][1]
    S_center[0] /= N
    S_center[1] /= N
    T_center[0] /= N
    T_center[1] /= N
    for i in range(N):
        S[i][0] -= S_center[0]
        S[i][1] -= S_center[1]
        T[i][0] -= T_center[0]
        T[i][1] -= T_center[1]
    #S,Tの中心を原点に移動した後のSを時計回りに90度回転させる
    for i in range(N):
        S[i][0],S[i][1] = S[i][1],-S[i][0]
    #S,Tの中心を原点に移動した後のSを時計回りに180度回転させる
    for i in range(N):
        S[i][0],S[i][1] = -S[i][0],-S[i][1]
    #S,Tの中心を原点に移動した後のSを時計回りに270度回転させる
    for i in range(N):
        S[i][0],S[i][1] = -S[i][1],S[i][0]
    #S,Tの中心を原点に移動した後のSを時計回りに360度回転させる
    for i in range(N):
        S[i][0],S[i][1] = S[i][0],S[i][1]
    #S,Tの中心を原点に移動した後のSを時
