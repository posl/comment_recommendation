Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())

=======
Suggestion 2

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if r >= w:
        print(w)
    else:
        print(r)

=======
Suggestion 3

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if r == w:
        print(1)
        return
    if r > w:
        print(w)
    else:
        print(r)

=======
Suggestion 4

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = n - r
    if r == 0 or w == 0:
        print(0)
    else:
        print(c[:r].count('W'))

=======
Suggestion 5

def main():
    n = int(input())
    stones = input()
    red = stones.count('R')
    ans = 0
    for i in range(red):
        if stones[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 6

def solve(n, c):
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    return w

=======
Suggestion 7

def main():
    N = int(input())
    c = input()
    #print(c)
    w = c.count('W')
    #print(w)
    r = c.count('R')
    #print(r)
    if w == 0 or r == 0:
        print(0)
        return
    i = 0
    j = N - 1
    cnt = 0
    while i < j:
        if c[i] == 'W' and c[j] == 'R':
            cnt += 1
            i += 1
            j -= 1
        elif c[i] == 'R' and c[j] == 'W':
            i += 1
            j -= 1
        elif c[i] == 'W':
            j -= 1
        elif c[j] == 'R':
            i += 1
        else:
            i += 1
            j -= 1
    print(cnt)
    return

=======
Suggestion 8

def problems174_d():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(n):
        if c[i] == "R":
            r += 1
    for i in range(r):
        if c[i] == "W":
            w += 1
    print(w)

=======
Suggestion 10

def main():
    N = int(input())
    c = input()
    #print(N)
    #print(c)
    #print(c[0])
    #print(c[1])
    #print(c[2])
    #print(c[3])
    #print(c[4])
    #print(c[5])
    #print(c[6])
    #print(c[7])
    #print(c[8])
    #print(c[9])
    #print(c[10])
    #print(c[11])
    #print(c[12])
    #print(c[13])
    #print(c[14])
    #print(c[15])
    #print(c[16])
    #print(c[17])
    #print(c[18])
    #print(c[19])
    #print(c[20])
    #print(c[21])
    #print(c[22])
    #print(c[23])
    #print(c[24])
    #print(c[25])
    #print(c[26])
    #print(c[27])
    #print(c[28])
    #print(c[29])
    #print(c[30])
    #print(c[31])
    #print(c[32])
    #print(c[33])
    #print(c[34])
    #print(c[35])
    #print(c[36])
    #print(c[37])
    #print(c[38])
    #print(c[39])
    #print(c[40])
    #print(c[41])
    #print(c[42])
    #print(c[43])
    #print(c[44])
    #print(c[45])
    #print(c[46])
    #print(c[47])
    #print(c[48])
    #print(c[49])
    #print(c[50])
    #print(c[51])
    #print(c[52])
    #print(c[53])
    #print(c[54])
    #print(c[55])
    #print(c[56])
    #print(c[57])
    #print(c[58])
    #print(c[59])
    #print(c[60])
    #print(c[61])
    #print(c[62])
    #print(c[63])
    #print(c[64])
    #print(c[65])
    #print(c[66])
    #print(c[67])
