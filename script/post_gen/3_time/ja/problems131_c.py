Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    A,B,C,D = map(int,input().split())
    #A,B,C,D = 4,9,2,3
    #A,B,C,D = 10,40,6,8
    #A,B,C,D = 314159265358979323,846264338327950288,419716939,937510582
    #print(A,B,C,D)
    #print(A/B,C/D)
    #print(A%B,C%D)
    #print(A//B,C//D)
    #print(A//C,B//C)
    #print(A//D,B//D)
    #print(A//C,B//C,A//D,B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D,A//C*B//C+A//D*B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D,A//C*B//C+A//D*B//D,A//C*B//C+A//D*B//D-A//C*B//C*A//D*B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D,A//C*B//C+A//D*B//D,A//C*B//C*A//D*B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D,A//C*B//C+A//D*B//D,A//C*B//C*A//D*B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D,A//C*B//C+A//D*B//D,A//C*B//C*A//D*B//D)
    #print(A//C,B//C,A//D,B//D,A//C*B//C,A//D*B//D,A//C*B//C+A//D*B//D,A//C*B//C*A//D*B//D)
    #print(A//C,B//C,A//D,B//

=======
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないものの個数を求めてください。
    # a 以上 b 以下の整数のうち、c でも d でも割り切れないもの

=======
Suggestion 5

def main():
    A,B,C,D = map(int,input().split())
    # A,B,C,D = 4,9,2,3
    # A,B,C,D = 10,40,6,8
    # A,B,C,D = 314159265358979323,846264338327950288,419716939,937510582

    # 全体の数
    all_num = B - A + 1
    # Cで割り切れる数
    C_num = B // C - (A-1) // C
    # Dで割り切れる数
    D_num = B // D - (A-1) // D
    # CとDで共通に割り切れる数
    CD_num = B // (C*D) - (A-1) // (C*D)

    print(all_num - C_num - D_num + CD_num)

=======
Suggestion 6

def main():
    A, B, C, D = map(int, input().split())
    CD = C*D//math.gcd(C, D)
    print(B-A+1-(B//C+B//D-B//CD)-(A//C+A//D-A//CD-1))

=======
Suggestion 7

def main():
    A,B,C,D=map(int,input().split())
    C1=B//C
    D1=B//D
    C2=(A-1)//C
    D2=(A-1)//D
    LCM=C*D//math.gcd(C,D)
    LCM1=B//LCM
    LCM2=(A-1)//LCM
    print(B-A+1-(C1-D1+LCM1)-(C2-D2+LCM2))

=======
Suggestion 8

def main():
    A,B,C,D = map(int,input().split())
    #print(A,B,C,D)

    #C,Dの最大公約数を求める
    #print(gcd(C,D))
    #C,Dの最小公倍数を求める
    #print(lcm(C,D))

    #A,B,C,Dの最小公倍数を求める
    #print(lcm(lcm(A,B),lcm(C,D)))

    #A,B,C,Dの最大公約数を求める
    #print(gcd(gcd(A,B),gcd(C,D)))

    #A,Bの最大公約数を求める
    #print(gcd(A,B))

    #A,Bの最小公倍数を求める
    #print(lcm(A,B))

    #A,B,C,Dの最小公倍数を求める
    #print(lcm(lcm(A,B),lcm(C,D)))

    #A,B,C,Dの最大公約数を求める
    #print(gcd(gcd(A,B),gcd(C,D)))

    #A,B,C,Dの最小公倍数を求める
    #print(lcm(lcm(A,B),lcm(C,D)))

    #A,B,C,Dの最大公約数を求める
    #print(gcd(gcd(A,B),gcd(C,D)))

    #A,B,C,Dの最小公倍数を求める
    #print(lcm(lcm(A,B),lcm(C,D)))

    #A,B,C,Dの最大公約数を求める
    #print(gcd(gcd(A,B),gcd(C,D)))

    #A,B,C,Dの最小公倍数を求める
    #print(lcm(lcm(A,B),lcm(C,D)))

    #A,B,C,Dの最大公約数を求める
    #print(gcd(gcd(A,B),gcd(C,D)))

    #A,B,C,Dの最小公倍数を求める
    #print(lcm(lcm(A,B),lcm(C,D)))

    #A,B,C,Dの最大公約数を求める
    #print(gcd(gcd(A,B),gcd(C,D)))
