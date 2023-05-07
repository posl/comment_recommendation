def main():
    #入力
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    
    #急行列車が止まる駅のリスト
    stop = []
    
    #急行列車が止まる駅のリストを作成
    for i in range(M):
        stop.append(T[i])
    
    #各駅に急行列車が止まるかどうか判定
    for i in range(N):
        if S[i] in stop:
            print("Yes")
        else:
            print("No")
