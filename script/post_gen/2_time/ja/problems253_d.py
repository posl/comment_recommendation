Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    sum = 0
    for i in range(1, N + 1):
        if i % A != 0 and i % B != 0:
            sum += i
    print(sum)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    c = n // a + n // b
    d = n // (a * b)
    print(n * (n + 1) // 2 - c * (c + 1) // 2 + d * (d + 1) // 2)

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    ans = 0
    ans += N // A * (A + 1) * A // 2
    ans += N // B * (B + 1) * B // 2
    ans -= N // (A * B) * (A * B + 1) * (A * B) // 2
    print(ans)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    print(N - (N//A + N//B - N//lcm(A,B)))

=======
Suggestion 6

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    # 3の倍数の個数
    count3 = N // A
    # 5の倍数の個数
    count5 = N // B
    # 15の倍数の個数
    count15 = N // (A * B)
    # 3の倍数の合計
    sum3 = count3 * (N - N % A + A) // 2
    # 5の倍数の合計
    sum5 = count5 * (N - N % B + B) // 2
    # 15の倍数の合計
    sum15 = count15 * (N - N % (A * B) + (A * B)) // 2
    # 3の倍数でも5の倍数でもない数の合計
    print(sum3 + sum5 - sum15)

=======
Suggestion 8

def lcm(a, b):
    return a * b // gcd(a, b)

N, A, B = map(int, input().split())

ans = (N // A) * (N // B) * lcm(A, B)
ans += (N // A) * (N % B)
ans += (N // B) * (N % A)
ans -= N // lcm(A, B)

print(ans)

=======
Suggestion 9

def main():
    n,a,b = map(int,input().split())
    #print(n,a,b)
    #print(n//a + n//b - n//lcm(a,b))
    print(n - n//a - n//b + n//lcm(a,b))

=======
Suggestion 10

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
