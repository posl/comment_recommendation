def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print(len(A))
    #Aの累積和を求める
    for i in range(1, len(A)):
        A[i] += A[i-1]
    #print(A)
    #Aの累積和をMで割った余りを求める
    for i in range(len(A)):
        A[i] %= M
    #print(A)
    #Aの累積和をMで割った余りの出現回数を求める
    #Aの累積和をMで割った余りが0の場合、1回出現する
    #Aの累積和をMで割った余りが1の場合、2回出現する
    #Aの累積和をMで割った余りが2の場合、3回出現する
    #...
    #Aの累積和をMで割った余りがM-1の場合、M回出現する
    #Aの累積和をMで割った余りがMの場合、1回出現する
    #Aの累積和をMで割った余りがM+1の場合、2回出現する
    #...
    #Aの累積和をMで割った余りが2M-1の場合、M+1回出現する
    #Aの累積和をMで割った余りが2Mの場合、1回出現する
    #Aの累積和をMで割った余りが2M+1の場合、2回出現する
    #...
    #Aの累積和をMで割った余りが3M-1の場合、M+2回出現する
    #Aの累積

if __name__ == '__main__':
    main()