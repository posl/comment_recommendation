Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i != N - 1:
                p[i], p[i + 1] = p[i + 1], p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == 0:
                p[i+1], p[i] = p[i], p[i+1]
            elif i == N-1:
                p[i-1], p[i] = p[i], p[i-1]
            else:
                p[i+1], p[i] = p[i], p[i+1]
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i+1 < N:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 5

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
        print(ans+1)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i],p[i+1] = p[i+1],p[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            if i != 0 and i != N-1:
                p[i],p[i+1] = p[i+1],p[i]
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    #print(P[0])
    #print(P[1])
    #print(P[2])
    #print(P[3])
    #print(P[4])
    #print(P[5])
    #print(P[6])
    #print(P[7])
    #print(P[8])
    #print(P[9])
    #print(P[10])
    #print(P[11])
    #print(P[12])
    #print(P[13])
    #print(P[14])
    #print(P[15])
    #print(P[16])
    #print(P[17])
    #print(P[18])
    #print(P[19])
    #print(P[20])
    #print(P[21])
    #print(P[22])
    #print(P[23])
    #print(P[24])
    #print(P[25])
    #print(P[26])
    #print(P[27])
    #print(P[28])
    #print(P[29])
    #print(P[30])
    #print(P[31])
    #print(P[32])
    #print(P[33])
    #print(P[34])
    #print(P[35])
    #print(P[36])
    #print(P[37])
    #print(P[38])
    #print(P[39])
    #print(P[40])
    #print(P[41])
    #print(P[42])
    #print(P[43])
    #print(P[44])
    #print(P[45])
    #print(P[46])
    #print(P[47])
    #print(P[48])
    #print(P[49])
    #print(P[50])
    #print(P[51])
    #print(P[52])
    #print(P[53])
    #print(P[54])
    #print(P[55])
    #print(P[56])
    #print(P[57])
    #print(P[58])
    #print(P[59])
    #print(P[60])
    #print(P[61])
    #print(P[62])
    #print(P[63])
    #print(P[64])
    #print(P[65])
    #print(P[66])
    #

=======
Suggestion 9

def main():
    N = int(input())
    p = list(map(int, input().split()))

    # 人 i の目の前にある料理の番号を p_i とする
    # p_i 番目の要素が i であるような配列を作る
    p_inv = [0] * N
    for i in range(N):
        p_inv[p[i]] = i

    # 人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[i] は i 番目の要素が p_i であることを意味する
    # つまり、p_inv[i] = p_i である

    # 人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[i] 番目の要素が i であることを意味する
    # つまり、p_inv[p_inv[i]] = i である

    # 人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[i] 番目の要素が i であることを意味する
    # つまり、p_inv[p_inv[i]] = i である
    # これは、人 i の目の前にある料理の番号を p_i とすると、
    # p_i 番目の要素が i であるような配列 p_inv に対し、
    # p_inv[p_i] 番目の要素が i であることを意味する
    #
