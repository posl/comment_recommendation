def main():
    #入力
    N, K = map(int, input().split()) #N個の食品 K個の嫌いな食品
    A = list(map(int, input().split())) #食品のおいしさ
    B = list(map(int, input().split())) #嫌いな食品番号
    #処理
    maxA = max(A) #おいしさが最大の食品のおいしさ
    if maxA in A: #おいしさが最大の食品があれば
        maxAindex = A.index(maxA) #おいしさが最大の食品の番号
        if maxAindex+1 in B: #嫌いな食品の番号と一致するなら
            print("Yes") #Yes
        else:
            print("No") #No
    else:
        print("No") #No
