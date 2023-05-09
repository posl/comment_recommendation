def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #初期化
    #B = []
    B = A
    #B = A * 100000
    sum = 0
    #Bを作成
    #for i in range(100000):
    #    B.extend(A)
    #Bを使ってsumを計算
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break
