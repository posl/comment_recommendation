def main():
    #入力
    T = int(input())
    N = [int(input()) for _ in range(T)]
    
    #処理
    #N=p^2q
    #p,qを求める
    #pは平方根をとる
    #qはNをpで割ったものの平方根をとる
    p = [int(N[i]**(1/2)) for i in range(T)]
    q = [int(N[i]/p[i]**2) for i in range(T)]
    
    #出力
    for i in range(T):
        print(p[i],q[i])

if __name__ == '__main__':
    main()