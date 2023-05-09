def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    #Aを10**100回連結した数列Bを作成
    B = A * (10**100)
    #Bの項を前から順に足したとき、和が初めてXを超えるのは何項目まで足したとき？を求める
    sum = 0
    for i in range(10**100):
        sum += B[i]
        if sum > X:
            print(i+1)
            break
