Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x // 2, a))

lcm = 1
for i in a:
    lcm = lcm * i // gcd(lcm, i)

for i in a:
    if (lcm // i) % 2 == 0:
        print(0)
        exit()

m = m // lcm
ans = (m + 1) // 2
print(ans)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 4

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x // 2, a))
lcm = 1
for i in range(n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
print((m // lcm + 1) // 2)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        c = a % b
        a = b
        b = c
    return a

=======
Suggestion 7

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n, m = map(int, input().split())
a = list(map(int, input().split()))

x = a[0] // 2
for i in range(1, n):
    x = lcm(x, a[i] // 2)

ans = m // x
print((ans + 1) // 2)

=======
Suggestion 8

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # まずは素因数分解して素因数のリストを作成
    A_factor = []
    for i in range(N):
        A_factor.append([])
        temp = A[i]
        for j in range(2, int(A[i]**(1/2))+1):
            while temp % j == 0:
                A_factor[i].append(j)
                temp //= j
        if temp != 1:
            A_factor[i].append(temp)
    # 素因数のリストを繋げる
    A_factor_all = []
    for i in range(N):
        A_factor_all += A_factor[i]
    # 素因数のリストから重複を削除
    A_factor_all = list(set(A_factor_all))
    # 素因数のリストから半公倍数を作成
    half_multiple = []
    for i in range(len(A_factor_all)):
        temp = A_factor_all[i]
        while temp <= M:
            half_multiple.append(temp)
            temp *= 2
    # 半公倍数のリストから重複を削除
    half_multiple = list(set(half_multiple))
    # 半公倍数のリストからAの要素の倍数を削除
    for i in range(N):
        for j in range(len(half_multiple)):
            if half_multiple[j] % A[i] == 0:
                half_multiple[j] = 0
    half_multiple = list(set(half_multiple))
    half_multiple.remove(0)
    # 半公倍数の個数を出力
    print(len(half_multiple))
