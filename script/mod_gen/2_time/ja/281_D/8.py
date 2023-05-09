def main():
    #入力
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    #Sの計算
    S = [0]
    for i in range(N):
        for j in range(len(S)):
            S.append(S[j]+A[i])
    #Sのソート
    S.sort()
    #SからDの倍数を削除
    S = [s for s in S if s%D != 0]
    #Sから最大値を出力
    if len(S) == 0:
        print(-1)
    else:
        print(S[len(S)-1])

if __name__ == '__main__':
    main()