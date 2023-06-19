Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [x-1 for x in P]

    count = 0
    for i in range(N):
        if P[i] == i:
            count += 1
            if i+1 < N:
                P[i], P[i+1] = P[i+1], P[i]
            else:
                P[i], P[0] = P[0], P[i]

    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int,input().split()))
    p.insert(0,0)
    p.append(0)
    ans = 0
    for i in range(1,n+1):
        if p[i-1] == i-1 or p[i+1] == i-1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
        elif p[p[i]] == i:
            count += 1
    if count == N:
        print(count)
    else:
        print(count+1)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]] = i
    ans = 0
    c = 0
    for i in range(n):
        if q[i] > c:
            c = q[i]
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    if N == 2:
        print(0)
        return
    if N == 3:
        if P[0] == 0 and P[1] == 1 and P[2] == 2:
            print(3)
            return
        else:
            print(2)
            return
    if N == 4:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3:
            print(4)
            return
        else:
            print(3)
            return
    if N == 5:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4:
            print(5)
            return
        else:
            print(4)
            return
    if N == 6:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4 and P[5] == 5:
            print(6)
            return
        else:
            print(5)
            return
    if N == 7:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4 and P[5] == 5 and P[6] == 6:
            print(7)
            return
        else:
            print(6)
            return
    if N == 8:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4 and P[5] == 5 and P[6] == 6 and P[7] == 7:
            print(8)
            return
        else:
            print(7)
            return
    if N == 9:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if p[i] == (i-1)%N or p[i] == (i+1)%N:
            count += 1

    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [i-1 for i in P]
    count = 0
    for i in range(N):
        if i == P[P[i]]:
            count += 1
    if count == N:
        print(N)
    else:
        print(count-1)

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    #print(n)
    #print(p)
    #print(len(p))
    #print(p[0])
    #print(p[1])
    #print(p[2])
    #print(p[3])
    #print(p[4])
    #print(p[5])
    #print(p[6])
    #print(p[7])
    #print(p[8])
    #print(p[9])
    #print(p[10])
    #print(p[11])
    #print(p[12])
    #print(p[13])
    #print(p[14])
    #print(p[15])
    #print(p[16])
    #print(p[17])
    #print(p[18])
    #print(p[19])
    #print(p[20])
    #print(p[21])
    #print(p[22])
    #print(p[23])
    #print(p[24])
    #print(p[25])
    #print(p[26])
    #print(p[27])
    #print(p[28])
    #print(p[29])
    #print(p[30])
    #print(p[31])
    #print(p[32])
    #print(p[33])
    #print(p[34])
    #print(p[35])
    #print(p[36])
    #print(p[37])
    #print(p[38])
    #print(p[39])
    #print(p[40])
    #print(p[41])
    #print(p[42])
    #print(p[43])
    #print(p[44])
    #print(p[45])
    #print(p[46])
    #print(p[47])
    #print(p[48])
    #print(p[49])
    #print(p[50])
    #print(p[51])
    #print(p[52])
    #print(p[53])
    #print(p[54])
    #print(p[55])
    #print(p[56])
    #print(p[57])
    #print(p[58])
    #print(p[59])
    #print(p[60])
    #print(p[61])
    #print(p[62])
    #print(p[63])
    #print(p[64])
    #print(p[65])
    #print
