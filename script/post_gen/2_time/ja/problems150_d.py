Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #A = [6,10]
    #M = 50
    #A = [14,22,40]
    #M = 100
    #A = [6,6,2,6,2]
    #M = 1000000000
    #A = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776,2199023255552,4398046511104,8796093022208,17592186044416,35184372088832,70368744177664,140737488355328,281474976710656,562949953421312,1125899906842624,2251799813685248,4503599627370496,9007199254740992,18014398509481984,36028797018963968,72057594037927936,144115188075855872,288230376151711744,576460752303423488,1152921504606846976,2305843009213693952,4611686018427387904,9223372036854775808,18446744073709551616,36893488147419103232,73786976294838206464,147573952589676412928,295147905179352825856,590295810358705651712,1180591620717411303424,2361183241434822606848,4722366482869645213696,9444732965739290427392,18889465931478580854784,37778931862957161709568,75557863725914323419136,151115727

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (M // A[i]) * (A[i] // 2)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += M // A[i]
        ans -= (M // (A[i] * 2)) - (M // (A[i] * 3))
    print(ans)

=======
Suggestion 4

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    LCM=1
    for a in A:
        LCM=LCM*a//gcd(LCM,a)
    ans=0
    for a in A:
        ans+=M//LCM*(LCM//a)
        if LCM//a%2==1:
            ans+=max(0,M%LCM-(LCM//a-1)//2)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求める
    def gcd(x, y):
        from fractions import gcd
        return gcd(x, y)
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求める
    def gcd(x, y):
        from fractions import gcd
        return gcd(x, y)
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求める
    def gcd(x, y):
        from fractions import gcd
        return gcd(x, y)
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求める
    def gcd(x, y):
        from fractions import gcd
        return gcd(x, y)
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求める
    def gcd(x, y):
        from fractions import gcd
        return gcd(x, y)
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求める
    def gcd(x, y):
        from fractions import gcd
        return gcd(x, y)
    #最小公倍数を求める
    def lcm(x, y):
        from fractions import gcd
        return (x * y) // gcd(x, y)
    #最大公約数を求め

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i//2 for i in a]
    c = 1
    for i in a:
        while i % 2 == 0:
            i //= 2
            c *= 2
    ans = (m//c + 1)//2
    print(ans)

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #Aの最小値
    a_min = min(A)
    #Aの最大値
    a_max = max(A)
    #Aの最大値以下の偶数の最大値
    a_max_even = a_max//2*2
    #Aの最小値以下の偶数の最大値
    a_min_even = a_min//2*2
    #Aの最大値以下の偶数の最大値以下の整数の最大値
    a_max_even_max = a_max_even//2
    #Aの最小値以下の偶数の最大値以下の整数の最大値
    a_min_even_max = a_min_even//2
    #Aの最大値以下の偶数の最大値以下の整数の最大値以下の整数の最大値
    a_max_even_max_max = a_max_even_max//2
    #Aの最小値以下の偶数の最大値以下の整数の最大値以下の整数の最大値
    a_min_even_max_max = a_min_even_max//2
    #Aの最大値以下の偶数の最大値以下の整数の最大値以下の整数の最大値以下の整数の最大値
    a_max_even_max_max_max = a_max_even_max_max//2
    #Aの最小値以下の偶数の最大値以下の整数の最大値以下の整数の最大値以下の整数の最大値
    a_min_even_max_max_max = a_min_even_max_max//2
    #Aの最大値以下��

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a//2 for a in A]
    A = list(set(A))
    N = len(A)
    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])
    if M < g:
        print(0)
    else:
        print((M//g+1)//2)
