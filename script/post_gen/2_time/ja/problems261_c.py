Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]]) + ")")
        else:
            d[s[i]] = 0
            print(s[i])

main()

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + '(' + str(d[s[i]]) + ')')
        else:
            d[s[i]] = 0
            print(s[i])

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = []
    for i in range(N):
        if S[i] in S[:i]:
            ans.append(S[i] + "(" + str(S[:i].count(S[i])) + ")")
        else:
            ans.append(S[i])
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    
    ans = []
    for i in range(N):
        if s[i] not in s[:i]:
            ans.append(s[i])
        else:
            ans.append(s[i] + "(" + str(s[:i].count(s[i])) + ")")
    
    for i in range(N):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S2 = []
    for i in range(N):
        if S[i] in S2:
            S[i] = S[i] + "(" + str(S2.count(S[i])) + ")"
            S2.append(S[i])
        else:
            S2.append(S[i])
    for i in range(N):
        print(S[i])

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S2 = []
    for s in S:
        if s in S2:
            S2.append(s+"("+str(S2.count(s))+")")
        else:
            S2.append(s)
    print(*S2, sep='

')

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = set()
    for i in range(N):
        if S[i] in T:
            print(S[i] + "(" + str(S[:i].count(S[i])) + ")")
        else:
            print(S[i])
        T.add(S[i])

main()

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(N)
    #print(S)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #

=======
Suggestion 9

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
