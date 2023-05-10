Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S2 = []
    for i in range(N):
        if S[i] in S2:
            index = S2.count(S[i])
            S2.append(S[i]+"("+str(index)+")")
        else:
            S2.append(S[i])
    for i in range(N):
        print(S2[i])

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(S)
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
            print(S[i]+'('+str(d[S[i]])+')')
        else:
            d[S[i]] = 0
            print(S[i])

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    #print(s.count('newfile'))
    #print(s.count('newfolder'))
    #print(s.count('newfile')+s.count('newfolder'))
    #print(s.count('newfile')+s.count('newfolder')+1)
    #print(s.count('newfile')+s.count('newfolder')+2)
    #print(s.count('newfile')+s.count('newfolder')+3)
    #print(s.count('newfile')+s.count('newfolder')+4)
    #print(s.count('newfile')+s.count('newfolder')+5)
    #print(s.count('newfile')+s.count('newfolder')+6)
    #print(s.count('newfile')+s.count('newfolder')+7)
    #print(s.count('newfile')+s.count('newfolder')+8)
    #print(s.count('newfile')+s.count('newfolder')+9)
    #print(s.count('newfile')+s.count('newfolder')+10)
    #print(s.count('newfile')+s.count('newfolder')+11)
    #print(s.count('newfile')+s.count('newfolder')+12)
    #print(s.count('newfile')+s.count('newfolder')+13)
    #print(s.count('newfile')+s.count('newfolder')+14)
    #print(s.count('newfile')+s.count('newfolder')+15)
    #print(s.count('newfile')+s.count('newfolder')+16)
    #print(s.count('newfile')+s.count('newfolder')+17)
    #print(s.count('newfile')+s.count('newfolder')+18)
    #print(s.count('newfile')+s.count('newfolder')+19)
    #print(s.count('newfile')+s.count('newfolder')+20)
    #print(s.count('newfile')+s.count('newfolder')+21)
    #print(s.count('newfile')+s.count('newfolder')+22)
    #print(s.count('newfile')+s.count('newfolder')+23)
    #print(s.count('newfile')+s.count('newfolder')+24)
    #print(s.count('newfile')+s.count('newfolder')+25)
    #print(s.count('newfile')+s.count('new

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        d[s] = d.get(s, 0) + 1
        if d[s] == 1:
            print(s)
        else:
            print(s + "(" + str(d[s] - 1) + ")")

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    s_dict = {}
    for s in S:
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1
    for s in S:
        if s_dict[s] > 1:
            print(s + "(" + str(s_dict[s] - 1) + ")")
        else:
            print(s)

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S2 = []
    for i in range(N):
        if S[i] in S2:
            cnt = 1
            while True:
                if S[i] + '(' + str(cnt) + ')' in S2:
                    cnt += 1
                else:
                    S2.append(S[i] + '(' + str(cnt) + ')')
                    break
        else:
            S2.append(S[i])
    for i in range(N):
        print(S2[i])

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    n = int(readline())
    d = {}
    for _ in range(n):
        s = readline().rstrip().decode('utf-8')
        if s not in d:
            d[s] = 0
        d[s] += 1
        print(s if d[s] == 1 else s+'('+str(d[s]-1)+')')

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S_ = []
    S_.append(S[0])
    for i in range(1,N):
        if S[i] in S_:
            S_.append(S[i]+"("+str(S_.count(S[i]))+")")
        else:
            S_.append(S[i])

    for i in range(N):
        print(S_[i])
main()

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
        if d[S[i]] == 1:
            print(S[i])
        else:
            print(S[i]+'('+str(d[S[i]])+')')
    return

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_dict = {}
    for i in range(N):
        if S[i] in S_dict:
            S_dict[S[i]] += 1
        else:
            S_dict[S[i]] = 1
        if S_dict[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + "(" + str(S_dict[S[i]]-1) + ")")
