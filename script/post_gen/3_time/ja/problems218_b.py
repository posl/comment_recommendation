Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = list(map(int, input().split()))
    S = []
    for i in range(26):
        S.append(chr(ord('a') + P[i] - 1))
    print(''.join(S))

=======
Suggestion 2

def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + i) for i in range(26)]
    for i in range(26):
        S[i], S[P[i] - 1] = S[P[i] - 1], S[i]
    print(''.join(S))

=======
Suggestion 3

def main():
    P = input().split()
    S = ""
    for i in range(26):
        S += chr(ord('a') + int(P[i]) - 1)
    print(S)

=======
Suggestion 4

def main():
    P = list(map(int, input().split()))
    S = ""
    for i in range(26):
        S += chr(97 + P[i] - 1)
    print(S)

=======
Suggestion 5

def main():
    P = list(map(int, input().split()))
    S = ''
    for i in range(26):
        S += chr(ord('a')+P[i]-1)
    print(S)

=======
Suggestion 6

def main():
    s = 'abcdefghijklmnopqrstuvwxyz'
    p = list(map(int, input().split()))
    for i in range(len(p)):
        print(s[p[i] - 1], end='')

=======
Suggestion 7

def main():
    p = list(map(int, input().split()))
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print(s[p[i]-1], end='')

=======
Suggestion 8

def main():
    P = list(map(int, input().split()))
    #print(P)
    S = ""
    for i in range(26):
        S = S + chr(ord('a') + P[i] - 1)
    print(S)

=======
Suggestion 9

def main():
    #入力
    P = list(map(int,input().split()))

    #処理
    S = ['a']*26
    for i in range(26):
        S[P[i]-1] = chr(97+i)

    #出力
    print(''.join(S))

=======
Suggestion 10

def main():
    #入力
    P = list(map(int,input().split()))

    #辞書順で小さい方からP_i番目の英小文字をリストに格納
    S = [chr(97+i) for i in range(26)]
    S = [S[i-1] for i in P]

    #出力
    print(*S,sep="")
