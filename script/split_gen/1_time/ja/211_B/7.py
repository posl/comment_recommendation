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
