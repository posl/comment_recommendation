Synthesizing 10/10 solutions

=======
Suggestion 1

def calc_abs_sum(x, y, z):
    return abs(x) + abs(y) + abs(z)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    cake = []
    for i in range(n):
        cake.append(list(map(int,input().split())))
    #print(cake)
    #print(cake[0][0])
    #print(cake[0][1])
    #print(cake[0][2])
    #print(cake[1][0])
    #print(cake[1][1])
    #print(cake[1][2])
    #print(cake[2][0])
    #print(cake[2][1])
    #print(cake[2][2])
    #print(cake[3][0])
    #print(cake[3][1])
    #print(cake[3][2])
    #print(cake[4][0])
    #print(cake[4][1])
    #print(cake[4][2])
    #print(cake[5][0])
    #print(cake[5][1])
    #print(cake[5][2])
    #print(cake[6][0])
    #print(cake[6][1])
    #print(cake[6][2])
    #print(cake[7][0])
    #print(cake[7][1])
    #print(cake[7][2])
    #print(cake[8][0])
    #print(cake[8][1])
    #print(cake[8][2])
    #print(cake[9][0])
    #print(cake[9][1])
    #print(cake[9][2])
    #print(cake[10][0])
    #print(cake[10][1])
    #print(cake[10][2])
    #print(cake[11][0])
    #print(cake[11][1])
    #print(cake[11][2])
    #print(cake[12][0])
    #print(cake[12][1])
    #print(cake[12][2])
    #print(cake[13][0])
    #print(cake[13][1])
    #print(cake[13][2])
    #print(cake[14][0])
    #print(cake[14][1])
    #print(cake[14][2])
    #print(cake[15][0])

=======
Suggestion 3

def main():
    # N, M = map(int, input().split())
    # cakes = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(cakes)
    # print(cakes[0][0])
    # print(cakes[1][0])
    # print(cakes[2][0])
    # print(cakes[3][0])
    # print(cakes[4][0])
    # print(cakes[0][1])
    # print(cakes[1][1])
    # print(cakes[2][1])
    # print(cakes[3][1])
    # print(cakes[4][1])
    # print(cakes[0][2])
    # print(cakes[1][2])
    # print(cakes[2][2])
    # print(cakes[3][2])
    # print(cakes[4][2])
    # print(cakes[0][0] + cakes[1][0] + cakes[2][0])
    # print(cakes[0][1] + cakes[1][1] + cakes[2][1])
    # print(cakes[0][2] + cakes[1][2] + cakes[2][2])
    # print(cakes[0][0] + cakes[1][0] + cakes[2][0] + cakes[3][0])
    # print(cakes[0][1] + cakes[1][1] + cakes[2][1] + cakes[3][1])
    # print(cakes[0][2] + cakes[1][2] + cakes[2][2] + cakes[3][2])
    # print(cakes[0][0] + cakes[1][0] + cakes[2][0] + cakes[3][0] + cakes[4][0])
    # print(cakes[0][1] + cakes[1][1] + cakes[2][1] + cakes[3][1] + cakes[4][1])
    # print(cakes[0][2] + cakes[1][2] + cakes[2][2] + cakes[3][2] + cakes[4][2])
    # print(cakes[0][0] + cakes[1][0] + cakes[2][0]

=======
Suggestion 4

def solve():
    # dp[i][j][k] := i番目までのケーキからj個選んだ時の, 人気度の合計の絶対値の最大値
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
    for i in range(n):
        for j in range(m+1):
            for k in range(2):
                for l in range(2):
                    for o in range(2):
                        if j == 0:
                            dp[l][o][1] = 0
                        else:
                            if k == 0:
                                if o == 0:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] + abs(x[i]))
                                else:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] + abs(y[i]))
                            else:
                                if o == 0:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] - abs(x[i]))
                                else:
                                    dp[l][o][1] = max(dp[l][o][1], dp[l][o][0] - abs(y[i]))
                        dp[l][o][0] = dp[l][o][1]
    print(dp[0][0][1])
    return

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        x, y, z = map(int, input().split())
        cakes.append([x, y, z])
    #print(cakes)

    ans = 0
    for i in range(2**3):
        plus_minus = []
        for j in range(3):
            if ((i >> j) & 1):
                plus_minus.append(-1)
            else:
                plus_minus.append(1)
        #print(plus_minus)

        sum_list = []
        for j in range(n):
            sum_list.append(cakes[j][0]*plus_minus[0] + cakes[j][1]*plus_minus[1] + cakes[j][2]*plus_minus[2])
        #print(sum_list)
        sum_list.sort(reverse=True)
        #print(sum_list)
        tmp = 0
        for j in range(m):
            tmp += sum_list[j]
        #print(tmp)
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    cakes.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)

    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for j in range(n):
            tmp.append(cakes[j][0] * ((i >> 0) & 1) + cakes[j][1] * ((i >> 1) & 1) + cakes[j][2] * ((i >> 2) & 1))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    # print(cakes)
    # print(n, m)
    # print(cakes[0][0])
    max_value = 0
    for i in range(2**3):
        # print(bin(i))
        # print(bin(i)[2:].zfill(3))
        # print(list(bin(i)[2:].zfill(3)))
        cake_list = list(bin(i)[2:].zfill(3))
        # print(cake_list)
        # print(cake_list[0])
        # print(cake_list[1])
        # print(cake_list[2])
        # print(cakes[0][0])
        # print(cakes[0][1])
        # print(cakes[0][2])
        # print(cakes[1][0])
        # print(cakes[1][1])
        # print(cakes[1][2])
        # print(cakes[2][0])
        # print(cakes[2][1])
        # print(cakes[2][2])
        # print(cakes[3][0])
        # print(cakes[3][1])
        # print(cakes[3][2])
        # print(cakes[4][0])
        # print(cakes[4][1])
        # print(cakes[4][2])
        # print(cake_list[0])
        # print(cake_list[1])
        # print(cake_list[2])
        # print(cakes[0][0] * int(cake_list[0]))
        # print(cakes[0][1] * int(cake_list[1]))
        # print(cakes[0][2] * int(cake_list[2]))
        # print(cakes[1][0] * int(cake_list[0]))
        # print(cakes[1][1] * int(cake_list[1]))
        # print(cakes[1][2] * int(cake_list[2]))
        # print(cakes[2][0] * int(cake_list[0]))
        # print(cakes[2][1] * int(cake_list[1]))
        # print(cakes[2][2] * int(cake_list[2]))
        # print

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    cake = []
    for i in range(n):
        x,y,z = map(int,input().split())
        cake.append([x,y,z])
    #print(cake)
    ans = 0
    for i in range(2**3):
        flag = [0]*3
        for j in range(3):
            if (i>>j)&1:
                flag[j] = 1
        #print(flag)
        cake.sort(key=lambda x: (flag[0]*x[0]-flag[1]*x[1]-flag[2]*x[2]),reverse=True)
        #print(cake)
        tmp = 0
        for j in range(m):
            tmp += abs(cake[j][0])+abs(cake[j][1])+abs(cake[j][2])
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 10

def solve():
    pass
