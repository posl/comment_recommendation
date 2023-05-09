def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(N)
    #print(S)
    #print(type(S))
    #print(type(S[0]))
    
    #Sの中の文字列をカウントする
    #Sの中の文字列をキーに、個数を値にする辞書を作る
    #Sの中身を順番に見ていく
    #Sの中身が辞書にないなら、そのまま出力する
    #Sの中身が辞書にあるなら、その値を1増やして出力する
    #辞書の値を1増やす
    
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
            print(S[i] + "(" + str(d[S[i]]) + ")")
        else:
            d[S[i]] = 0
            print(S[i])

if __name__ == '__main__':
    main()