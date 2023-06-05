Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(h, w):
    #h1, h2, h3 = h
    #w1, w2, w3 = w
    #print(h1, h2, h3)
    #print(w1, w2, w3)
    #print('-----')
    #print(h1+h2+h3)
    #print(w1+w2+w3)
    #print('-----')
    #print('-----')
    #print('-----')
    #print

=======
Suggestion 2

def f(h1, h2, h3, w1, w2, w3):
    import math
    from functools import reduce
    from itertools import permutations
    def comb(n, r):
        if n == 0 or r == 0:
            return 1
        else:
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    def comb_with_repetition(n, r):
        return comb(n + r - 1, r)

    def perm(n, r):
        return math.factorial(n) // math.factorial(n - r)

    def perm_with_repetition(n, r):
        return n ** r

    def m(n, r):
        return reduce(lambda x, y: x * y, range(n, n - r, -1), 1)

=======
Suggestion 3

def f(x):
    if x == 1:
        return 1
    else:
        return x*f(x-1)

=======
Suggestion 4

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)

=======
Suggestion 5

def f(h1,h2,h3,w1,w2,w3):
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+w1!=h2+w2 or h2+w2!=h3+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1+h2+h3!=w1+w2+w3:
        return 0

    return 1

h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(f(h1,h2,h3,w1,w2,w3))

=======
Suggestion 6

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    ans = 0
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                if i+j+k==h1 and i+j+k==h2 and i+j+k==h3 and i+j+k==w1 and i+j+k==w2 and i+j+k==w3:
                    ans += 1
    print(ans)

=======
Suggestion 7

def solve(h1,h2,h3,w1,w2,w3):
    ans = 0
    for a in range(1,10000):
        for b in range(1,10000):
            for c in range(1,10000):
                if a+b+c == h1 and a+b+c == h2 and a+b+c == h3 and a+b+c == w1 and a+b+c == w2 and a+b+c == w3:
                    ans += 1
    print(ans)


h1,h2,h3,w1,w2,w3 = map(int,input().split())
solve(h1,h2,h3,w1,w2,w3)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    h1,h2,h3,w1,w2,w3=map(int,input().split())
    res=0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if i+j+k==h1 and i+j+k==h2 and i+j+k==h3 and i+j+k==w1 and i+j+k==w2 and i+j+k==w3:
                    res+=1
    print(res)

=======
Suggestion 10

def calc(a, b, c, d, e, f):
    # 1. 3*3のマス目に入る数字の合計はa+b+c+d+e+f
    # 2. 3*3のマス目に入る数字の合計は3*(1+2+3+4+5+6+7+8+9) = 135
    # 3. 1+2+3+4+5+6+7+8+9 = 45
    # 4. 135 - (a+b+c+d+e+f) = g
    # 5. gは1~9のいずれか
    # 6. 1~9のいずれかの数字をa~fに足すと45になる
    # 7. a~fに足す数字の組み合わせは、1~9の数字の中からgを除いて5つ選ぶ組み合わせ
    # 8. 8C5 = 56通り
    # 9. 56通りの組み合わせのうち、a+b+c = h1, d+e+f = h2, a+d = w1, b+e = w2, c+f = w3を満たす組み合わせを求める
    # 10. a+b+c = h1を満たす組み合わせは、gを除いた8通り
    # 11. d+e+f = h2を満たす組み合わせは、gを除いた8通り
    # 12. a+d = w1を満たす組み合わせは、gを除いた8通り
    # 13. b+e = w2を満たす組み合わせは、gを除いた8通り
    # 14. c+f = w3を満たす組み合わせは、gを除いた8通り
    # 15. 8*8*8*8*8 = 32768通り
