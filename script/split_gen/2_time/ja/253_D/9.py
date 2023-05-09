def main():
    N,A,B = map(int,input().split())
    #A,Bの最大公約数を求める
    #最大公約数を求める関数
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a%b)
    #最小公倍数を求める関数
    def lcm(a,b):
        return a*b//gcd(a,b)
    #A,Bの最小公倍数を求める
    C = lcm(A,B)
    #A,Bの最小公倍数で割り切れる数の個数を求める
    D = N//C
    #Aで割り切れる数の個数を求める
    E = N//A
    #Bで割り切れる数の個数を求める
    F = N//B
    #A,Bの最小公倍数で割り切れる数の個数を引く
    G = E+F-D
    #答えを求める
    print(N*(N+1)//2-G*C)
