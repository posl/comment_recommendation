Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for _ in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)

    ans = 0
    for i in range(2**N):
        p = 1
        for j in range(N):
            if (i >> j) & 1:
                p *= A[j][0]
            else:
                p *= A[j][1]
        if p <= X:
            ans += 1
    print(ans)

=======
Suggestion 2

def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2 ** N):
        c = 1
        for j in range(N):
            if (i >> j) & 1:
                c *= L[j][(i >> j) & 1]
        if c == X:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    L = [a[0] for a in A]
    B = [a[1:] for a in A]
    ans = 0
    for b in product(*B):
        p = 1
        for i in range(N):
            p *= b[i]
        if p == X:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(2**N):
        p = 1
        for j in range(N):
            if (i>>j)&1:
                p *= L[j][(i>>j)&1]
        if p == X:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    n, x = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    d = defaultdict(int)
    for i in range(n):
        for j in range(1, l[i][0]+1):
            d[l[i][j]] += 1
    ans = 0
    for i in d:
        if i != 1 and x % i == 0 and d[x//i] > 0:
            if i == x // i:
                ans += d[i] * (d[i]-1) // 2
            else:
                ans += d[i] * d[x//i]
    print(ans)

=======
Suggestion 7

def main():
    #入力
    N,X = map(int,input().split())
    L = []
    for i in range(N):
        l = list(map(int,input().split()))
        L.append(l)
    
    #処理
    #N個のリストを作る
    #それぞれのリストの中にはXの約数が入っている
    #リストの中のリストの中のリストを作る
    #それぞれのリストの中のリストの中にはXの約数が入っている
    #Xの約数のリストの中のリストの中のリストを作る
    #それぞれのリストの中のリストの中のリストの中にはXの約数が入っている
    #N個のリストの中のリストの中のリストの中のリストの中にはXの約数が入っている
    #リストの中のリストの中のリストの中のリストの中のリストの中にはXの約数が入っている
    #リストの中のリストの中のリストの中のリストの中のリストの中のリストの中にはXの約数が入

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    # 約数全列挙
    def divisor(n):
        i = 1
        table = []
        while i * i <= n:
            if n % i == 0:
                table.append(i)
                if i != n // i:
                    table.append(n // i)
            i += 1
        return table

    # 約数の個数を求める
    def count_divisor(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt

    # 約数の個数を求める
    def count_divisor2(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt

    # 約数の個数を求める
    def count_divisor3(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt

    # 約数の個数を求める
    def count_divisor4(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
            i += 1
        return cnt

    # 約数の個数を求める
    def count_divisor5(n):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt

=======
Suggestion 9

def get_primes(n):
    # n以下の素数を列挙する
    if n < 2:
        return []
    elif n == 2:
        return [2]
    else:
        primes = [2]
        for i in range(3, n+1, 2):
            for p in primes:
                if i%p == 0:
                    break
            else:
                primes.append(i)
        return primes

=======
Suggestion 10

def   solve ( N ,   X ,   A ): 
     # dp[i][j] = the number of ways to choose the first i bags 
     # so that the product of the numbers written on the chosen balls is j 
     dp   =   [ [ 0 ]   *   ( X   +   1 )   for   _   in   range ( N   +   1 )] 
     dp [ 0 ][ 1 ]   =   1 
     for   i   in   range ( N ): 
         for   j   in   range ( X   +   1 ): 
             for   k   in   range ( 1 ,   A [ i ][ 0 ]   +   1 ): 
                 if   j   *   A [ i ][ k ]   <=   X : 
                     dp [ i   +   1 ][ j   *   A [ i ][ k ]]   +=   dp [ i ][ j ] 
     return   dp [ N ][ X ]
