def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aをソート
    A.sort()
    #Aの最大値がA[0]に来るようにする
    A.reverse()
    #Aの要素の個数を数える
    count = [0] * (A[0]+1)
    for i in range(N):
        count[A[i]] += 1
    #countを累積和
    for i in range(1,A[0]+1):
        count[i] += count[i-1]
    #出力
    print(sum(count))

if __name__ == '__main__':
    main()