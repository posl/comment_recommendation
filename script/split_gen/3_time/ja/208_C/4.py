def main():
    #N:国民の人数
    #K:高橋君が持っているお菓子の個数
    N, K = map(int, input().split())
    #a:国民の国民番号
    a = list(map(int, input().split()))
    #aを国民番号の昇順にソート
    a.sort()
    #KをNで割った商と余りを求める
    quo = K // N
    rem = K % N
    #余りが0なら全員にquo個ずつ配る
    if rem == 0:
        for i in range(N):
            print(quo)
    #余りが0でないなら
    else:
        #余りの数だけa[0]からa[rem-1]までの国民に1個ずつ配る
        for i in range(rem):
            print(quo+1)
        #余りの数だけa[rem]からa[N-1]までの国民にquo個ずつ配る
        for i in range(rem, N):
            print(quo)
