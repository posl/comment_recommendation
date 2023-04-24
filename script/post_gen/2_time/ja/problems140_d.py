Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "L":
            ans += 1
        else:
            break
    for i in range(N-1, -1, -1):
        if S[i] == "R":
            ans += 1
        else:
            break
    if ans < N:
        if K >= 1:
            ans += 2 * K - 1
    print(min(ans, N))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "R":
            ans += 1
            break
    for i in range(N-1, -1, -1):
        if S[i] == "L":
            ans += 1
            break
    ans += 2 * min(K, S.count("RL"))
    print(min(ans, N))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'L':
            ans += 1
            if i+1 < N and S[i+1] == 'R':
                ans += 1
        else:
            if i+1 < N and S[i+1] == 'L':
                ans += 1
    print(min(2*N-1, ans+2*K))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    LR = []
    for i in range(N):
        if i == 0:
            LR.append([S[i], 1])
        elif S[i] == LR[-1][0]:
            LR[-1][1] += 1
        else:
            LR.append([S[i], 1])
    if len(LR) == 1:
        print(N)
        return
    if LR[0][0] == "R":
        LR.insert(0, ["L", 0])
    if LR[-1][0] == "L":
        LR.append(["R", 0])
    ans = 0
    for i in range(0, len(LR), 2):
        ans += LR[i][1] + LR[i+1][1]
    if len(LR) // 2 <= K:
        print(N)
        return
    for i in range(1, len(LR), 2):
        if i // 2 > K:
            break
        tmp = 0
        for j in range(i, len(LR), 2):
            tmp += LR[j][1] + LR[j+1][1]
            if j // 2 + (len(LR)-j-1) // 2 > K:
                break
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    S = input()

    S = S.replace("R", "1").replace("L", "0")
    S = S.replace("1", "R").replace("0", "L")

    ans = 0
    for i in range(N):
        if S[i] == "R":
            r = i
            for j in range(i, N):
                if S[j] == "L":
                    l = j
                    break
            else:
                l = N
            ans += min(r - i + l - r, K) * 2 + 1
            i = l
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    # 0: L, 1: R
    A = [0 if s == 'L' else 1 for s in S]
    # print(A)

    # 連続する区間を数える
    # 例えば、LRRLRLRRLRLLR ならば、[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] を
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12] に分ける
    # このとき、[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] は、
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 の区間のうち、
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 は、
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 の区間のうち、
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 は、
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 が連続する区間となる
    # このとき、連続する区間の長さは 11 である
    # このように、連続する区間の長さを数えていくことで、
    # 適切な操作を行うことで、幸福な人

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
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
    #print(S

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    S = input()

    ans = 0
    # まず、全ての人が幸福である場合をカウントする
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ans += 1
    # 次に、操作を行う。操作を行うと、幸福でない人が幸福になる場合がある。
    # その場合、幸福でない人の数が 2 減る。
    # また、操作を行うと、幸福でない人が幸福になる場合がある。
    # その場合、幸福でない人の数が 2 増える。
    # 以上から、操作を行うと、幸福でない人の数が 2K 減る。
    # これを考慮すると、幸福でない人の数が 2K 以下である場合の最大値を求める。
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            continue
        if i - 1 >= 0 and S[i - 1] == S[i + 1]:
            ans = max(ans, 2 * K + 1)
        else:
            ans = max(ans, 2 * K)
    # 操作を行わない場合と、操作を行う場合の最大値を比較する
    print(max(ans, N - 1))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K)
    #print(S)

    # 1. LRLRRL -> LRRLLR
    # 2. LRRLLR -> RLLRRL
    # 3. RLLRRL -> RRRLLL
    # 4. RRRLLL -> LLLRRR
    # 5. LLLRRR -> LRLRRL
    # 6. LRLRRL -> LRRLLR
    # 7. LRRLLR -> RLLRRL
    # 8. RLLRRL -> RRRLLL
    # 9. RRRLLL -> LLLRRR
    # 10. LLLRRR -> LRLRRL
    # 11. LRLRRL -> LRRLLR
    # 12. LRRLLR -> RLLRRL
    # 13. RLLRRL -> RRRLLL
    # 14. RRRLLL -> LLLRRR
    # 15. LLLRRR -> LRLRRL
    # 16. LRLRRL -> LRRLLR
    # 17. LRRLLR -> RLLRRL
    # 18. RLLRRL -> RRRLLL
    # 19. RRRLLL -> LLLRRR
    # 20. LLLRRR -> LRLRRL
    # 21. LRLRRL -> LRRLLR
    # 22. LRRLLR -> RLLRRL
    # 23. RLLRRL -> RRRLLL
    # 24. RRRLLL -> LLLRRR
    # 25. LLLRRR -> LRLRRL
    # 26. LRLRRL -> LRRLLR
    # 27. LRRLLR -> RLLRRL
    # 28. RLLRRL -> RRRLLL
    # 29. RRRLLL -> LLLRRR
    # 30. LLLRRR -> LRLRRL
    # 31. LRLRRL -> LRRLLR
    # 32. LRRLLR -> RLLRRL

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()
    # 1. LRLRRL という状態になっているとき、
    #    LRLRRL という状態になっている人は幸福なので、
    #    LRLRRL という状態になっている人の数を数える。
    # 2. LRLRRL という状態になっている人の数を数える。
    # 3. 1. と 2. のうち大きい方を出力する。
    # 4. 1. と 2. のうち小さい方を出力する。
    # 5. 1. と 2. のうち大きい方が K 回以上の操作を行える場合、
    #    1. と 2. のうち小さい方を出力する。
    # 6. 1. と 2. のうち大きい方が K 回以下の操作を行える場合、
    #    1. と 2. のうち大きい方を出力する。
    # 7. 1. と 2. のうち小さい方が K 回以上の操作を行える場合、
    #    1. と 2. のうち大きい方を出力する。
    # 8. 1. と 2. のうち小さい方が K 回以下の操作を行える場合、
    #    1. と 2. のうち小さい方を出力する。
    # 9. 1. と 2. のうち大きい方が K 回以上の操作を行える場合、
    #    1. と 2. のうち小さい方を出力する。
    # 10. 1. と 2. のうち大きい方が K 回以下の操作を行える場
