Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N // 2):
        if S[i] != S[N - i - 1]:
            ans += min(A, B)
    if N % 2 == 1:
        ans += B
    print(ans)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] != S[-1-i]:
            ans += min(A, B)
    print(ans)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    S = input()

    if S == S[::-1]:
        print(0)
        return

    if A > B:
        print(0)
        return

    if S[0] != S[-1]:
        print(A)
        return

    cnt = 1
    for i in range(N):
        if S[i] != S[-i-1]:
            break
        cnt += 1

    if cnt == N:
        print((N-1)*B)
        return

    if cnt == N-1:
        print(A)
        return

    if S[0] == S[-1]:
        print((cnt//2)*B + A)
        return

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    S = input()
    if A > B:
        print(N * B)
        return
    if len(set(S)) == 1:
        print(N * A // 2)
        return
    cnt = 0
    for i in range(N):
        if S[i] != S[N - i - 1]:
            cnt += 1
    if cnt == 1:
        print(N * A - A // 2)
        return
    print(N * A)

=======
Suggestion 5

def solve():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        print(ans)
        return
    if N % 2 == 0:
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
        print(ans)
        return
    else:
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
        for i in range(N//2+1):
            if S[i] != S[N-1-i]:
                ans += min(A, B)
                print(ans)
                return
        print(ans)
        return
solve()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    S = input()
    #print(N, A, B, S)
    #print(S[0], S[1], S[2], S[3], S[4], S[5], S[6], S[7])

    #回文でない文字列の数をカウント
    count = 0
    for i in range((N+1)//2):
        if S[i] != S[N-1-i]:
            count += 1

    #print(count)
    if count == 0:
        print(0)
    elif A < B:
        print(A*count)
    else:
        print(B*count)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    S = input()
    if N == 1:
        print(0)
        return

    # 連続する同じ文字の個数をカウント
    # 例: S = "rrefa" なら cnt = [2, 1, 1]
    cnt = []
    now = S[0]
    cnt_now = 1
    for i in range(1, N):
        if S[i] == now:
            cnt_now += 1
        else:
            cnt.append(cnt_now)
            now = S[i]
            cnt_now = 1
    cnt.append(cnt_now)
    # print(cnt)

    # 連続する同じ文字の個数を使って、
    # 1. 全て同じ文字の場合
    # 2. 2 文字のみ違う場合
    # 3. 3 文字のみ違う場合
    # 4. 4 文字のみ違う場合
    # 5. それ以外
    # の場合を考える
    # 1. 全て同じ文字の場合
    # 1 文字のみ違う場合と同じ
    # 2. 2 文字のみ違う場合
    # 2 文字のみ違う場合と同じ
    # 3. 3 文字のみ違う場合
    # 2 文字のみ違う場合と同じ
    # 4. 4 文字のみ違う場合
    # 2 文字のみ違う場合と同じ
    # 5. それ以外
    # 2 文字のみ違う場合と同じ

    # 1. 全て同じ文字の場合
    if len(cnt) == 1:
        print(0)
        return
    # 2. 2 文字のみ違う場合
    if len(cnt) == 2:
        print(min(A, B))
        return
    # 3. 3 文字

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    S = input()
    #print(N, A, B, S)
    #print(S)
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

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    S = input()
    #print(N, A, B, S)
    #print(S[0], S[1])
    #print(S[0:2])
    #print(S[0:2] == S[2:4])

    #文字数が奇数の場合
    if N % 2 == 1:
        #前半と後半が同じかどうか判定
        if S[0:int(N/2)] == S[int(N/2+1):N][::-1]:
            print(0)
        else:
            print(min(A, B))
    #文字数が偶数の場合
    else:
        #前半と後半が同じかどうか判定
        if S[0:int(N/2)] == S[int(N/2):N][::-1]:
            print(0)
        else:
            #前半と後半が同じ文字数かどうか判定
            if S[0:int(N/2)] == S[int(N/2):N]:
                print(B)
            else:
                print(min(A, B))

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    S = input()
    S = S + S
    #print(S)

    #Sの中で、S[i] == S[i+N]の数を数える
    cnt = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt += 1
    #print(cnt)

    #Sの中で、S[i] == S[i+N]の数を数える
    cnt2 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt2 += 1
    #print(cnt2)

    #Sの中で、S[i] == S[i+N]の数を数える
    cnt3 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt3 += 1
    #print(cnt3)

    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt4 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt4 += 1
    #print(cnt4)

    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt5 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt5 += 1
    #print(cnt5)

    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt6 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt6 += 1
    #print(cnt6)

    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt7 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt7 += 1
    #print(cnt7)

    #A円で一回操作した時に、Sの中で、
