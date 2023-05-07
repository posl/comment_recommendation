def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #Aの最大値を求める
    max_A = max(A)
    #print(max_A)
    #Aの最大値+1で初期化したリストを作る
    B = [0] * (max_A+1)
    #print(B)
    #Aの要素をBのインデックスにする
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    #Bの要素をインデックスにする
    for i in range(max_A+1):
        if B[i] == 0:
            print(i)
            break
    else:
        print(max_A+1)

if __name__ == '__main__':
    main()