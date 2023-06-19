Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n**0.5)+1):
        x = i*i
        while x <= n:
            ans -= 1
            x *= i
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n**0.5)+1):
        j = 2
        while i**j <= n:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 3

def solve(n):
    num = 0
    for i in range(2, int(n**0.5)+1):
        x = i
        while x <= n:
            x *= i
            num += 1
    return n - num

=======
Suggestion 4

def main():
    n = int(input())
    a = set()
    for i in range(2, int(n**0.5)+1):
        x = i*i
        while x <= n:
            a.add(x)
            x *= i
    print(n-len(a))

=======
Suggestion 5

def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        if i ** 2 > N:
            break
        tmp = i ** 2
        while tmp <= N:
            ans -= 1
            tmp *= i
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = int(n ** 0.5)
    b = int(n ** 0.25)
    print(n - a - b + 1)

=======
Suggestion 7

def main():
    n = int(input())
    # 1,2,3,5,6,7
    # 4,8
    # 9,16
    # 25,36
    # 49,64
    # 81,100
    # 121,144
    # 169,196
    # 225,256
    # 289,324
    # 361,400
    # 441,484
    # 529,576
    # 625,676
    # 729,784
    # 841,900
    # 961,1024
    # 1089,1156
    # 1225,1296
    # 1369,1444
    # 1521,1600
    # 1681,1764
    # 1849,1936
    # 2025,2116
    # 2209,2304
    # 2401,2500
    # 2601,2704
    # 2809,2916
    # 3025,3136
    # 3249,3364
    # 3481,3600
    # 3721,3844
    # 3969,4096
    # 4225,4356
    # 4489,4624
    # 4761,4900
    # 5041,5184
    # 5329,5476
    # 5625,5776
    # 5929,6084
    # 6241,6400
    # 6561,6724
    # 6889,7056
    # 7225,7396
    # 7569,7744
    # 7921,8100
    # 8281,8464
    # 8649,8836
    # 9025,9216
    # 9409,9604
    # 9801,10000
    # 10201,10404
    # 10609,10816
    # 11025,11236
    # 11449,11664
    # 11881,12100
    # 12321,12544
    # 127

=======
Suggestion 8

def get_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return primes

=======
Suggestion 9

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
A = set()
for i in range(2, int(N**0.5)+1):
    if i**2 > N:
        break
    x = i**2
    while x <= N:
        A.add(x)
        x *= i
print(N - len(A))
