Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = [input() for i in range(4)]
    if s.count("H") == 1 and s.count("2B") == 1 and s.count("3B") == 1 and s.count("HR") == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = [input() for _ in range(4)]
    if s.count("H") == 1 and s.count("2B") == 1 and s.count("3B") == 1 and s.count("HR") == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = [input() for _ in range(4)]
    if S.count('H') == 1 and S.count('2B') == 1 and S.count('3B') == 1 and S.count('HR') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    #入力
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()

    #H , 2B , 3B , HR がそれぞれ 1 つずつあるか判定
    if (S_1 == "H" or S_2 == "H" or S_3 == "H" or S_4 == "H") and (S_1 == "2B" or S_2 == "2B" or S_3 == "2B" or S_4 == "2B") and (S_1 == "3B" or S_2 == "3B" or S_3 == "3B" or S_4 == "3B") and (S_1 == "HR" or S_2 == "HR" or S_3 == "HR" or S_4 == "HR"):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    #入力
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    #判定
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    #入力
    s = [input() for i in range(4)]
    #出力
    if s.count('H') == 1 and s.count('2B') == 1 and s.count('3B') == 1 and s.count('HR') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = [input() for _ in range(4)]
    print("Yes" if len(set(S)) == 4 else "No")

=======
Suggestion 8

def main():
    #入力
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()

    #S1~S4の中にH,2B,3B,HRがあるかどうかを判定する
    #H,2B,3B,HRの数をカウントする
    count = 0
    if S1 == "H":
        count += 1
    if S2 == "H":
        count += 1
    if S3 == "H":
        count += 1
    if S4 == "H":
        count += 1
    if S1 == "2B":
        count += 1
    if S2 == "2B":
        count += 1
    if S3 == "2B":
        count += 1
    if S4 == "2B":
        count += 1
    if S1 == "3B":
        count += 1
    if S2 == "3B":
        count += 1
    if S3 == "3B":
        count += 1
    if S4 == "3B":
        count += 1
    if S1 == "HR":
        count += 1
    if S2 == "HR":
        count += 1
    if S3 == "HR":
        count += 1
    if S4 == "HR":
        count += 1

    #H,2B,3B,HRの数が4つならYes、そうでないならNoを出力する
    if count == 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    #文字列の入力
    #文字列の入力
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()

    #文字列のリスト化
    S = [S_1,S_2,S_3,S_4]

    #リストの中の文字列の数をカウント
    H = S.count("H")
    B2 = S.count("2B")
    B3 = S.count("3B")
    HR = S.count("HR")

    #文字列の数が1ならYes、それ以外ならNoを出力
    if H == 1 and B2 == 1 and B3 == 1 and HR == 1:
        print("Yes")
    else:
        print("No")
