Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == (i - 1) % n or p[i] == i or p[i] == (i + 1) % n:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, -1)
    ans = 0
    for i in range(1, n + 1):
        if p[i] == i - 1:
            ans += 1
            p[i] = p[i + 1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            if P[i] == N-1 or P[i] == 1:
                count += 1
        elif i == N-1:
            if P[i] == 0 or P[i] == N-2:
                count += 1
        else:
            if P[i] == i-1 or P[i] == i+1:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [i - 1 for i in p]

    cnt = 0
    for i in range(n):
        if p[p[i]] == i:
            cnt += 1
    print(cnt // 2)

=======
Suggestion 5

def main():
    # 读取输入
    n = int(input())
    p = [int(i) for i in input().split()]

    # 计算答案
    ans = 0
    for i in range(n):
        if p[i] == (p[(i-1) % n] + 1) % n or p[i] == (p[(i+1) % n] + 1) % n:
            ans += 1

    # 输出答案
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    max = 0
    happy = 0
    for i in range(N):
        if p[i] == i:
            happy += 1
            if happy > max:
                max = happy
        else:
            happy = 0
    print(max)

=======
Suggestion 7

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
Suggestion 8

def solve():
    N = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1 and p[i+1] == i+1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    P = list(map(int, input().split()))

    # 人iが幸福かどうかを表す値
    # 0: 不幸
    # 1: 幸福
    # 2: 未定
    status = [2] * N

    # 幸福な人の数
    happy_count = 0

    while True:
        # 幸福な人の数を更新
        happy_count += status.count(1)

        # 幸福な人の数が変わらなかったら終了
        if happy_count == N:
            break

        # 幸福な人の数を更新
        happy_count = 0

        # 人iが幸福かどうかを更新
        for i in range(N):
            if status[i] == 1:
                continue

            # 人iの前の人の番号
            prev = (i - 1 + N) % N

            # 人iの後ろの人の番号
            next = (i + 1) % N

            # 人iの前の人が幸福なら人iは幸福
            if status[prev] == 1:
                status[i] = 1

            # 人iの後ろの人が幸福なら人iは幸福
            elif status[next] == 1:
                status[i] = 1

        # 転置
        P = [P[p] for p in P]

    # 幸福な人の数を出力
    print(happy_count)

=======
Suggestion 10

def get_max_happy_persons(N, p):
    #print(N, p)
    #print("p[0]=", p[0])
    #print("p[1]=", p[1])
    #print("p[2]=", p[2])
    #print("p[3]=", p[3])
    #print("p[4]=", p[4])
    #print("p[5]=", p[5])
    #print("p[6]=", p[6])
    #print("p[7]=", p[7])
    #print("p[8]=", p[8])
    #print("p[9]=", p[9])
    #print("p[10]=", p[10])
    #print("p[11]=", p[11])
    #print("p[12]=", p[12])
    #print("p[13]=", p[13])
    #print("p[14]=", p[14])
    #print("p[15]=", p[15])
    #print("p[16]=", p[16])
    #print("p[17]=", p[17])
    #print("p[18]=", p[18])
    #print("p[19]=", p[19])
    #print("p[20]=", p[20])
    #print("p[21]=", p[21])
    #print("p[22]=", p[22])
    #print("p[23]=", p[23])
    #print("p[24]=", p[24])
    #print("p[25]=", p[25])
    #print("p[26]=", p[26])
    #print("p[27]=", p[27])
    #print("p[28]=", p[28])
    #print("p[29]=", p[29])
    #print("p[30]=", p[30])
    #print("p[31]=", p[31])
    #print("p[32]=", p[32])
    #print("p[33]=", p[33])
    #print("p[34]=", p[34])
    #print("p[35]=", p[35])
    #print("p[36]=", p[36])
    #
