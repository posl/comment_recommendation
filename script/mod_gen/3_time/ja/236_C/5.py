def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(N, M)
    #print(S)
    #print(T)
    #急行列車が止まる駅のリストを作成
    stop = []
    for i in range(M):
        stop.append(T[i])
    #print(stop)
    #急行列車が止まるかどうか判定
    for i in range(N):
        if S[i] in stop:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()