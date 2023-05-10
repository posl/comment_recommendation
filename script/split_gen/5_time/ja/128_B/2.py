def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    #print(S)
    #print(P)
    #辞書順でソート
    SP = sorted(zip(S, P), key=lambda x: x[0])
    #print(SP)
    #辞書順でソートしたリストを点数降順でソート
    SPP = sorted(SP, key=lambda x: x[1], reverse=True)
    #print(SPP)
    #点数降順でソートしたリストを辞書順でソート
    SPPP = sorted(SPP, key=lambda x: x[0])
    #print(SPPP)
    #リストの要素から点数だけを取り出して出力
    for i in range(N):
        print(SPPP[i][1])
