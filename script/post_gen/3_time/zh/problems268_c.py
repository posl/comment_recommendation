Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == 0:
                if p[-1] == N - 1:
                    ans += 1
            else:
                if p[i - 1] == i - 1:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
    if ans == N:
        print(N)
    else:
        print(ans+2)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.append(0)
    result = 0
    for i in range(1, n+1):
        if p[i-1] == i or p[i+1] == i:
            result += 1
    print(result)

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))

    # 从左到右，从右到左的最大连续数
    left = [0] * N
    right = [0] * N

    # 从左到右，从右到左的最大连续数
    for i in range(N-1):
        if p[i] < p[i+1]:
            left[i+1] = left[i] + 1

    for i in range(N-1, 0, -1):
        if p[i-1] < p[i]:
            right[i-1] = right[i] + 1

    # 从左到右，从右到左的最大连续数
    for i in range(N):
        if p[i] < p[(i+1)%N]:
            left[i] = left[(i+1)%N] + 1

    for i in range(N-1, -1, -1):
        if p[i] < p[(i-1)%N]:
            right[i] = right[(i-1)%N] + 1

    ans = 0
    for i in range(N):
        ans = max(ans, left[i]+right[i]+1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    #读入数据
    N = int(input())
    p = [int(i) for i in input().split()]
    #初始化
    ans = 0
    for i in range(N):
        if p[i] == (i-1)%N or p[i] == i or p[i] == (i+1)%N:
            ans += 1
    #输出
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]] = i
    ans = 0
    cnt = 0
    for i in range(n):
        if q[i] > cnt:
            cnt = q[i]
        else:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == (i - 1) % N or p[i] == i or p[i] == (i + 1) % N:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
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
