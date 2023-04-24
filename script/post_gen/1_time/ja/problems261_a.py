Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 <= L2 or R2 <= L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 2

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 <= L2:
        print(0)
    elif R2 <= L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 3

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 <= L2 or L1 >= R2:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))
main()

=======
Suggestion 4

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if r1 <= l2 or r2 <= l1:
        print(0)
    else:
        print(min(r1,r2)-max(l1,l2))

=======
Suggestion 5

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 <= l2:
        print(0)
    elif r1 <= r2:
        print(r1 - l2)
    elif r2 <= l1:
        print(0)
    elif r2 <= r1:
        print(r2 - l1)
    else:
        print(r1 - l1)

=======
Suggestion 6

def main():
    L_1, R_1, L_2, R_2 = map(int, input().split())

    # 両方の色で塗られている部分の長さ
    ans = 0

    # 青色の塗り始める座標が赤色の塗り終わる座標よりも小さい場合
    if L_2 < R_1:
        # 青色の塗り終わる座標が赤色の塗り始める座標よりも大きい場合
        if R_2 > L_1:
            # 青色の塗り始める座標が赤色の塗り始める座標よりも大きい場合
            if L_2 > L_1:
                # 青色の塗り終わる座標が赤色の塗り終わる座標よりも小さい場合
                if R_2 < R_1:
                    ans = R_2 - L_2
                # 青色の塗り終わる座標が赤色の塗り終わる座標よりも大きい場合
                else:
                    ans = R_1 - L_2
            # 青色の塗り始める座標が赤色の塗り始める座標よりも小さい場合
            else:
                # 青色の塗り終わる座標が赤色の塗り終わる座標よりも小さい場合
                if R_2 < R_1:
                    ans = R_2 - L_1
                # 青色の塗り終わる座標が赤色の塗り終わる座標よりも大きい場合
                else:
                    ans =

=======
Suggestion 7

def main():
    #入力
    L1, R1, L2, R2 = map(int, input().split())
    #処理
    if R1 <= L2 or R2 <= L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 8

def main():
    #入力
    L1, R1, L2, R2 = map(int, input().split())

    #処理
    if R1 < L2 or R2 < L1:
        print(0)
    else:
        print(min(R1,R2) - max(L1,L2))

=======
Suggestion 9

def main():
    #入力
    L1, R1, L2, R2 = map(int, input().split())
    #処理
    if R1 <= L2:
        ans = 0
    elif R2 <= L1:
        ans = 0
    else:
        ans = min(R1, R2) - max(L1, L2)
    #出力
    print(ans)

=======
Suggestion 10

def main():
    #入力
    L1, R1, L2, R2 = map(int, input().split())
    #処理
    if R1 <= L2:
        print(0)
    elif R2 <= L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))
