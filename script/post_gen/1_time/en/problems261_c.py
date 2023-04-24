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
            print(s[i] + '(' + str(d[s[i]]) + ')')
        else:
            d[s[i]] = 0
            print(s[i])

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]]) + ")")

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    D = {}
    for s in S:
        if s not in D:
            D[s] = 1
            print(s)
        else:
            print(s + '(' + str(D[s]) + ')')
            D[s] += 1
    return

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = dict()
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 0
        if D[s] == 0:
            print(s)
        else:
            print(s+'('+str(D[s])+')')

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for s in S:
        if s in cnt:
            cnt[s] += 1
            print(s + '(' + str(cnt[s]) + ')')
        else:
            cnt[s] = 0
            print(s)

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    d = {}
    for s in S:
        if s not in d:
            d[s] = 0
            print(s)
        else:
            d[s] += 1
            print(s + "(" + str(d[s]) + ")")

main()

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_dict = {}
    for i in range(N):
        if S[i] in S_dict:
            S_dict[S[i]] += 1
            S[i] += '(' + str(S_dict[S[i]]) + ')'
        else:
            S_dict[S[i]] = 0
    for i in range(N):
        print(S[i])

=======
Suggestion 8

def main():
    #N = int(input())
    #S = [input() for _ in range(N)]
    N = 11
    S = ['a','a','a','a','a','a','a','a','a','a','a']
    #print(N)
    #print(S)
    #print(len(S))
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
    #print

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(S)
    #print(N)
    #print(S)
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
    #print(S[65
