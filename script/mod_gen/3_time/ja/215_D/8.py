def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #Aの最大値を求める
    A_max = max(A)
    #Aの最大値を超えるMまでの素数リストを作る
    prime_list = [True] * (M+1)
    prime_list[0] = False
    prime_list[1] = False
    for i in range(2,int(M**0.5)+1):
        if prime_list[i]:
            for j in range(i*2,M+1,i):
                prime_list[j] = False
    #Aの最大値を超えるMまでの素数リストのindexを取得
    prime_list_index = [i for i, x in enumerate(prime_list) if x == True]
    #Aの最大値を超えるMまでの素数リストのindexのうち、Aの最大値を超えるMまでの素数リストのindexの最小のものを取得
    prime_list_index_min = min([i for i in prime_list_index if i > A_max])
    #Aの最大値を超えるMまでの素数リストのindexのうち、Aの最大値を超えるMまでの素数リストのindexの最小のものからMまでの素数リストを取得
    prime_list = prime_list[prime_list_index_min:]
    #Aの最大値を超えるMまでの素数リストのindexのうち、Aの最大値を超えるMまでの素数リストのindexの最小のものからMまでの素数リストのindexを取得
    prime_list_index = [i for i, x in enumerate(prime_list) if x == True]
    #Aの最大値を超えるMまでの素数リストのindexのうち、Aの最大値を超えるMまでの素数リストのindexの最小のものからMまでの素数リストのindexの最大のもの

if __name__ == '__main__':
    main()