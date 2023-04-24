Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = [input() for _ in range(9)]

    ans = 0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i + k < 9 and j + l < 9:
                        if S[i][j] == '#' and S[i][j + l] == '#' and S[i + k][j] == '#' and S[i + k][j + l] == '#':
                            ans += 1

    print(ans)

=======
Suggestion 2

def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(7):
        for j in range(7):
            if S[i][j] == "#" and S[i][j+1] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#":
                count += 1
    print(count)

=======
Suggestion 3

def main():
    S = []
    for i in range(9):
        S.append(input())
    ans = 0
    for i in range(7):
        for j in range(7):
            if S[i][j] == "#" and S[i][j+1] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#":
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                for k in range(9):
                    if S[i][k] == '.' or S[k][j] == '.':
                        break
                else:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = [input() for _ in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if i+1 < 9 and j+1 < 9 and S[i][j] == S[i+1][j] == S[i][j+1] == S[i+1][j+1] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    S = []
    for i in range(9):
        S.append(list(input()))
    
    ans = 0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i == k and j == l:
                        continue
                    if i == k or j == l:
                        continue
                    if abs(i - k) == abs(j - l):
                        continue
                    if S[i][j] == "#" and S[k][l] == "#":
                        x1 = min(i, k)
                        x2 = max(i, k)
                        y1 = min(j, l)
                        y2 = max(j, l)
                        if x2 - x1 == y2 - y1:
                            if S[x1][y1] == "#" and S[x2][y2] == "#":
                                ans += 1
    print(ans//2)

=======
Suggestion 7

def main():
    s = []
    for i in range(9):
        s.append(input())
    #print(s)

    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                for k in range(9):
                    for l in range(9):
                        if s[k][l] == "#":
                            for m in range(9):
                                for n in range(9):
                                    if s[m][n] == "#":
                                        for o in range(9):
                                            for p in range(9):
                                                if s[o][p] == "#":
                                                    if (i,j) != (k,l) and (i,j) != (m,n) and (i,j) != (o,p) and (k,l) != (m,n) and (k,l) != (o,p) and (m,n) != (o,p):
                                                        if (i,j) == (min(i,j,k,l,m,n,o,p),max(i,j,k,l,m,n,o,p)) and (k,l) == (min(i,j,k,l,m,n,o,p),max(i,j,k,l,m,n,o,p)+1) and (m,n) == (min(i,j,k,l,m,n,o,p)+1,max(i,j,k,l,m,n,o,p)) and (o,p) == (min(i,j,k,l,m,n,o,p)+1,max(i,j,k,l,m,n,o,p)+1):
                                                            count += 1
    print(count//24)

=======
Suggestion 8

def check(x, y):
    if x < 0 or x > 8 or y < 0 or y > 8:
        return False
    return True

=======
Suggestion 9

def main():
    #入力
    S = []
    for i in range(9):
        S.append(input())
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[0][7])
    #print(S[0][8])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[1][5])
    #print(S[1][6])
    #print(S[1][7])
    #print(S[1][8])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[2][5])
    #print(S[2][6])
    #print(S[2][7])
    #print(S[2][8])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print(S[3][5])
    #print(S[3][6])
    #print(S[3][7])
    #print(S[3][8])
    #print(S[4][0])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[4][4])
    #print(S[4][5])
    #print(S[4][6])
    #print(S[4][7])
    #print(S[4][8])
    #print(S[5][0])
    #print(S[5][1])
    #print(S[5][2])
    #print(S[5][3])
    #print(S[5][4])
    #print(S[5][5])
    #print(S[5][6])
    #print

=======
Suggestion 10

def main():
    #入力
    S = [input() for i in range(9)]
    #出力
    print(Solve(S))
