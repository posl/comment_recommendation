Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(i, x, s):
    if i == n:
        return s
    if s == 'AND':
        return dfs(i + 1, x, s) + dfs(i + 1, x + 1, s)
    else:
        return dfs(i + 1, x, s) * 2 + dfs(i + 1, x + 1, s)


n = int(input())
s = [input() for _ in range(n)]
print(dfs(0, 0, s[0]))

=======
Suggestion 2

def solve(n, s):
    if n == 0:
        return 1
    elif s[n - 1] == 'AND':
        return solve(n - 1, s)
    elif s[n - 1] == 'OR':
        return 2 ** (n + 1) + solve(n - 1, s)

n = int(input())
s = [input() for _ in range(n)]
print(solve(n, s))

=======
Suggestion 3

def main():
    #N = int(input())
    #S = []
    #for i in range(N):
    #    S.append(input())
    N = 60
    S = []
    for i in range(N):
        S.append("OR")
    #print(N)
    #print(S)
    #print(S.count("AND"))
    #print(S.count("OR"))
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
    #

=======
Suggestion 4

def solve(n, s):
    ans = 1
    for i in range(n):
        if s[i] == 'OR':
            ans += 2**(i+1)
    return ans

=======
Suggestion 5

def main():
    N=int(input())
    S=[]
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    ans=0
    for i in range(N):
        if S[i]=="OR":
            ans+=2**(i+1)
    ans+=1
    print(ans)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1
    for i in range(n):
        if s[i] == "OR":
            ans += 2 ** (i + 1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    #print(N)
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
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 1
    for i in range(n):
        if s[i] == "OR":
            ans += 2**(i+1)
    print(ans)
