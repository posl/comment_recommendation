Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    h = [int(i) for i in input().split()]
    h.insert(0,0)
    h.append(0)
    count = 0
    for i in range(1,N+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            count += 1
        elif h[i-1] > h[i] and h[i] < h[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    h = list(map(int, input().split()))
    print(h)

=======
Suggestion 3

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        l = 0
        r = 0
        for i in range(n):
            if h[i] > 0:
                l = i
                break
        for i in range(l, n):
            if h[i] == 0:
                r = i - 1
                break
            elif i == n - 1:
                r = i
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)

=======
Suggestion 4

def input():
    n = int(input())
    h = list(map(int, input().split()))
    return n, h

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    #print(n)
    #print(h)
    #print(len(h))
    #print(type(h))
    #print(h[0])
    #print(h[1])
    #print(h[2])
    #print(h[3])
    #print(h[4])
    #print(h[5])
    #print(h[6])
    #print(h[7])
    #print(h[8])
    #print(h[9])
    #print(h[10])
    #print(h[11])
    #print(h[12])
    #print(h[13])
    #print(h[14])
    #print(h[15])
    #print(h[16])
    #print(h[17])
    #print(h[18])
    #print(h[19])
    #print(h[20])
    #print(h[21])
    #print(h[22])
    #print(h[23])
    #print(h[24])
    #print(h[25])
    #print(h[26])
    #print(h[27])
    #print(h[28])
    #print(h[29])
    #print(h[30])
    #print(h[31])
    #print(h[32])
    #print(h[33])
    #print(h[34])
    #print(h[35])
    #print(h[36])
    #print(h[37])
    #print(h[38])
    #print(h[39])
    #print(h[40])
    #print(h[41])
    #print(h[42])
    #print(h[43])
    #print(h[44])
    #print(h[45])
    #print(h[46])
    #print(h[47])
    #print(h[48])
    #print(h[49])
    #print(h[50])
    #print(h[51])
    #print(h[52])
    #print(h[53])
    #print(h[54])
    #print(h[55])
    #print(h[56])
    #print(h[57])
    #print(h[58])
    #print(h[59])
    #print(h[60])
    #print(h[61])
    #print(h[62])
    #print(h[63])
    #print(h[64])
    #print(h

=======
Suggestion 6

def water_flower(N, h):
    count = 0
    while True:
        l = 0
        r = 0
        for i in range(N):
            if h[i] != 0:
                l = i
                break
        for i in range(N-1, -1, -1):
            if h[i] != 0:
                r = i
                break
        if l == r:
            count += h[l]
            break
        count += max(h[l:r+1])
        for i in range(l, r+1):
            h[i] -= max(h[l:r+1])
    return count

=======
Suggestion 7

def water_the_flowers(N, H):
    ans = 0
    for i in range(N):
        ans += H[i]
    return ans

=======
Suggestion 8

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        i = 0
        while i < N:
            if h[i] > 0:
                ans += 1
                while i < N and h[i] > 0:
                    h[i] -= 1
                    i += 1
            i += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    while True:
        if max(h) == 0:
            break
        else:
            for i in range(n):
                if h[i] > 0:
                    count += 1
                    h[i] -= 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    h.insert(0,0)
    h.append(0)
    ans = 0
    for i in range(1,N+2):
        if h[i-1] < h[i]:
            ans += h[i] - h[i-1]
    print(ans)
