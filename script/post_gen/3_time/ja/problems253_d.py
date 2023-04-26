Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print(N - (N // A + N // B - N // (A * B)))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    #Aの倍数の数
    A_count = N//A
    #Bの倍数の数
    B_count = N//B
    #AとBの最小公倍数
    C = A*B//math.gcd(A,B)
    #Cの倍数の数
    C_count = N//C
    #AとBの最小公倍数を含む総和
    print(A_count*B_count*C_count - C_count*(C_count+1)//2*C)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print((N//A + N//B) - (N//lcm(A,B)))

=======
Suggestion 4

def main():
    #入力
    N,A,B = map(int, input().split())
    #処理
    sum = 0
    for i in range(1,N+1):
        if i % A != 0 and i % B != 0:
            sum += i
    #出力
    print(sum)

=======
Suggestion 5

def main():
    N,A,B=map(int,input().split())
    Alist = list(range(0,N+1,A))
    Blist = list(range(0,N+1,B))
    Clist = list(set(Alist+Blist))
    Clist.sort()
    print(sum(Clist))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    # 3の倍数の総和
    s3 = A*(N//A)*(N//A+1)//2
    # 5の倍数の総和
    s5 = B*(N//B)*(N//B+1)//2
    # 15の倍数の総和
    s15 = A*B*(N//(A*B))*(N//(A*B)+1)//2
    print(s3+s5-s15)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    # 総和を求める
    sum = 0
    # N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    for i in range(1, N+1):
        if i % A != 0 and i % B != 0:
            sum += i
    print(sum)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    # 全体からaの倍数+bの倍数の和を引く
    # aの倍数+bの倍数はaとbの最小公倍数の倍数
    # aとbの最小公倍数 = a*b / 最大公約数
    # 最大公約数はユークリッドの互除法を使う
    print(n * (n + 1) // 2 - (n // a + n // b - n // (a * b // gcd(a, b))) * (n // a + n // b - n // (a * b // gcd(a, b)) + 1) // 2)
