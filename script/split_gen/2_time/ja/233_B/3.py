def reverse(L,R,S):
    #L,Rの間の文字を逆順にする
    #L,Rは1から始まるので、-1する
    #文字列のスライスは、[始まり:終わり]となるので、-1する
    #文字列のスライスは、[始まり:終わり:間隔]となるので、-1する
    #文字列のスライスは、[始まり:終わり:間隔]となるので、-1する
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    return S
