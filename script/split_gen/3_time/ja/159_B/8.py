def main():
    #入力
    S = input()
    #Sの長さ
    N = len(S)
    #Sの1文字目から(N-1)/2文字目まで(両端含む)からなる文字列
    S1 = S[0:int((N-1)/2)]
    #Sの(N+3)/2文字目からN文字目まで(両端含む)からなる文字列
    S2 = S[int((N+3)/2-1):N]
    #Sが強い回文かどうかを判定して出力
    if S == S[::-1] and S1 == S1[::-1] and S2 == S2[::-1]:
        print('Yes')
    else:
        print('No')
