Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     P   =   list ( map ( int ,   input (). split ())) 
     ans   =   "" 
     for   i   in   range ( 1 ,   27 ): 
         ans   +=   chr ( P . index ( i )   +   ord ( "a" )) 
     print ( ans )

=======
Suggestion 2

def main():
    P = list(map(int, input().split()))
    S = [chr(97 + i) for i in range(26)]
    for i in range(26):
        S[i], S[P[i] - 1] = S[P[i] - 1], S[i]
    print(''.join(S))

=======
Suggestion 3

def main():
    P = list(map(int, input().split()))
    S = ''
    for i in range(26):
        S += chr(ord('a') + P.index(i+1))
    print(S)

=======
Suggestion 4

def main():
    P = list(map(int,input().split()))
    S = [chr(ord('a') + i) for i in range(26)]
    for i in range(26):
        S[P[i] - 1] = chr(ord('a') + i)
    print(''.join(S))

=======
Suggestion 5

def main():
    p = list(map(int,input().split()))
    s = ""
    for i in range(26):
        s += chr(ord('a') + p[i] - 1)
    print(s)

=======
Suggestion 6

def main():
    P = list(map(int, input().split()))
    #print(P)
    S = ""
    for i in range(26):
        S += chr(ord('a') + P[i] - 1)
    print(S)

=======
Suggestion 7

def main():
    #入力
    P = list(map(int, input().split()))
    #出力
    print(''.join([chr(i+96) for i in P]))

main()

=======
Suggestion 8

def main():
    input = sys.stdin.readline
    #入力
    P = list(map(int, input().split()))
    # 出力
    for i in range(26):
        print(chr(ord('a') + P[i] - 1), end = '')

=======
Suggestion 9

def main():
    #入力
    P = list(map(int,input().split()))
    
    #出力
    print("".join([chr(ord("a")+i-1) for i in P]))

=======
Suggestion 10

def main():
    #入力
    P = list(map(int,input().split()))
    #辞書順のアルファベットをリスト化
    alpha = list(map(chr, range(97, 123)))
    #出力
    for i in range(len(P)):
        print(alpha[P[i]-1],end="")
