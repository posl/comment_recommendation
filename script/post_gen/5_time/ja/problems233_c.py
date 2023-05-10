Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    bags = []
    for i in range(N):
        bag = list(map(int, input().split()))
        bags.append(bag)
    ans = 0
    for i in range(1, 2**N):
        total = 1
        for j in range(N):
            if (i >> j) & 1:
                total *= bags[j][0]
        if total == X:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())

    balls = []
    for i in range(N):
        balls.append(list(map(int, input().split())))

    #print(N, X)
    #print(balls)

    # ビット探索
    # 2^N通りの取り出し方がある
    # それぞれの取り出し方について、総積がXになるかどうかを調べる
    # 計算量は、O(2^N * N)
    # 2^N * N = 2^18 * 18 = 262144
    # 2^N = 2^18 = 262144

    # 2^N通りの取り出し方を調べる
    # 取り出し方は、0 or 1 で表す
    # 例えば、N=2の場合、00, 01, 10, 11の4通り
    # 0の場合、袋1からボールを取り出さない
    # 1の場合、袋1からボールを取り出す
    # 0の場合、袋2からボールを取り出さない
    # 1の場合、袋2からボールを取り出す
    # 例えば、N=3の場合、000, 001, 010, 011, 100, 101, 110, 111の8通り

    # 2^N通りの取り出し方を調べる
    # 例えば、N=2の場合、00, 01, 10, 11の4通り
    # 0の場合、袋1からボールを取り出さない
    # 1の場合、袋1からボールを取り出す
    # 0の場合、袋2からボールを取り出さない
    # 1の場合、袋2からボール

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))

    #print(n, x)
    #print(l)

    #print(2**n)

    #for i in range(2**n):
    #    print(i)

    #print(bin(2**n))

    #print(bin(2**n)[2:])
    #print(len(bin(2**n)[2:]))

    #print(bin(2**n)[2:].zfill(n))
    #print(len(bin(2**n)[2:].zfill(n)))

    #print(bin(2**n)[2:].zfill(n)[::-1])

    #print(bin(2**n)[2:].zfill(n)[::-1].count('1'))

    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1)

    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0)

    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 1)

    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 2)

    #print(bin(2**n)[2:].zfill(n)[::-1].count('1') == 1 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 0 and bin(2**n)[2:].zfill(n)[::-1].index('1') == 1 and bin(2**n)[2:].

=======
Suggestion 4

def main():
    N,X = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    for i in range(N):
        A.append(L[i][1:])
    from itertools import product
    ans = 0
    for i in product(*A):
        if sum(i) == X:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    #print(N, X)
    #print(L)
    #print(A)
    #print(L[0])
    #print(A[0])
    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[2][2])
    #print(A[0][0] * A[1][0])
    #print(A[0][0] * A[1][1])
    #print(A[0][0] * A[1][2])
    #print(A[0][1] * A[1][0])
    #print(A[0][1] * A[1][1])
    #print(A[0][1] * A[1][2])
    #print(A[0][2] * A[1][0])
    #print(A[0][2] * A[1][1])
    #print(A[0][2] * A[1][2])
    #print(A[0][0] * A[1][0] * A[2][0])
    #print(A[0][0] * A[1][0] * A[2][1])
    #print(A[0][0] * A[1][0] * A[2][2])
    #print(A[0][0] * A[1][1] * A[2][0])
    #print(A[0][0] * A[1][1] * A[2][1])
    #print(A[0][0] * A[1][1] * A[2][2])
    #print(A[0][0] * A[1][2] * A[2][0])
    #print(A[0][0] * A[1][2] * A[2][1])
    #print(A[0][0

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    bags = []
    for _ in range(n):
        bags.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 2**n):
        tmp = i
        sum = 1
        for j in range(n):
            if tmp % 2 == 1:
                sum *= bags[j][0]
            tmp //= 2
        if sum == x:
            ans += 1
    print(ans)

=======
Suggestion 7

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N,X = map(int,input().split())

balls = []
for i in range(N):
    balls.append(list(map(int,input().split())))

ans = 0
for i in range(1,2**N):
    tmp = 1
    for j in range(N):
        if i>>j & 1:
            tmp *= balls[j][0]
    if X%tmp == 0:
        divisors = make_divisors(X//tmp)
        for divisor in divisors:
            if divisor <= balls[j][0]:
                ans += 1
print(ans)

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    L = []
    a = []
    for i in range(N):
        L.append(list(map(int,input().split())))
        a.append(L[i][1:])
    #print(L)
    #print(a)
    #print(list(itertools.product(*a)))
    #print(list(itertools.chain.from_iterable(itertools.product(*a))))
    #print(list(itertools.chain.from_iterable(itertools.product(*a))))
    print(len([i for i in list(itertools.chain.from_iterable(itertools.product(*a))) if i == X]))
    #print(list(itertools.chain.from_iterable(itertools.product(*a))).count(X))

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ans = 0
    for i in range(N):
        if len(A[i]) == 1:
            if X % A[i][0] == 0:
                ans += 1
        else:
            for j in range(L[i]):
                if X % A[i][j] == 0:
                    ans += 1
    print(ans)
