Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def main():
    A, B, C, D = map(int, input().split())
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないもの

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def main():
    A,B,C,D = map(int,input().split())
    ans = B - A + 1
    ans -= B // C - (A - 1) // C
    ans -= B // D - (A - 1) // D
    ans += B // (C * D // gcd(C,D)) - (A - 1) // (C * D // gcd(C,D))
    print(ans)

=======
Suggestion 5

def main():
    A,B,C,D = map(int,input().split())
    print(B-A+1-(B//C-(A-1)//C)-(B//D-(A-1)//D)+((B//C)*(B//D)-(A-1)//C*(A-1)//D))
main()

=======
Suggestion 6

def main():
    A, B, C, D = map(int, input().split())
    E = C * D
    F = B // C - (A - 1) // C
    G = B // D - (A - 1) // D
    H = B // E - (A - 1) // E
    ans = B - A + 1 - (F + G - H)
    print(ans)

=======
Suggestion 7

def gcd(a,b):
    if b > a:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())
    #c,dの最小公倍数
    e = c*d//gcd(c,d)
    print(b-a+1-(b//c+b//d-b//e-(a-1)//c-(a-1)//d+(a-1)//e))
