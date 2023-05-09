def check(S,T):
    #x=0,1,...,|T| に対して次の問題を解いてください。
    for x in range(len(T)+1):
        #S の先頭の x 文字と末尾の |T|-x 文字を順番を保ったまま連結することで得られる長さ |T| の文字列を S' とする。
        S1 = S[:x]
        S2 = S[-(len(T)-x):]
        S3 = S1 + S2
        #S' と T がマッチするならば Yes と、そうでなければ No と出力せよ。
        if S3 == T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    check()