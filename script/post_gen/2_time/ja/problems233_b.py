Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L, R = map(int, input().split())
    S = input()
    print(S[:L-1] + S[L-1:R][::-1] + S[R:])

=======
Suggestion 2

def main():
    L,R = map(int,input().split())
    S = input()
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    print(S)

=======
Suggestion 3

def main():
    l, r = map(int, input().split())
    s = input()
    print(s[0:l-1] + s[l-1:r][::-1] + s[r:])

=======
Suggestion 4

def reverse(L,R,S):
    #L,Rの間の文字を逆順にする
    #L,Rは1から始まるので、-1する
    #文字列のスライスは、[始まり:終わり]となるので、-1する
    #文字列のスライスは、[始まり:終わり:間隔]となるので、-1する
    #文字列のスライスは、[始まり:終わり:間隔]となるので、-1する
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    return S
