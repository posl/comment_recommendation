Synthesizing 10/10 solutions

=======
Suggestion 1

def prime_factorization(n):
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

=======
Suggestion 2

def main():
    K = int(input())
    N = 1
    for i in range(2,K+1):
        N *= i
        if N % K == 0:
            print(i)
            return

=======
Suggestion 3

def main():
    K = int(input())
    N = K
    i = 2
    while i * i <= K:
        if K % i == 0:
            while K % i == 0:
                K //= i
            N = N // i * (i - 1)
        i += 1
    if K != 1:
        N = N // K * (K - 1)
    print(N)

=======
Suggestion 4

def main():
    k = int(input())
    ans = 1
    for i in range(2, k):
        ans *= i
        if ans % k == 0:
            print(i)
            break
    else:
        print(k)

=======
Suggestion 5

def main():
    K = int(input())
    N = 1
    while K > 1:
        if K % 2 == 0:
            K = K // 2
        elif K % 5 == 0:
            K = K // 5
        else:
            break
        N += 1
    print(N)

=======
Suggestion 6

def main():
    K = int(input())
    ans = 1
    for i in range(2,K+1):
        ans *= i
        if ans%K == 0:
            print(i)
            exit()
    print(K)

=======
Suggestion 7

def main():
    k = int(input())
    n = 1
    while True:
        if n % k == 0:
            print(n)
            break
        else:
            n += 1

=======
Suggestion 8

def main():
    K = int(input())
    N = 1
    while True:
        if N % K == 0:
            print(N)
            break
        N += 1

=======
Suggestion 9

def main():
    k = int(input())
    n = 1
    while True:
        if n % k == 0:
            print(n)
            break
        n += 1

=======
Suggestion 10

def prime_factorization(n):
    # 素因数分解
    # n:整数
    # 戻り値:素因数分解結果
    # 例:prime_factorization(24)
    # 戻り値: [2, 2, 2, 3]
    # 24 = 2^3 * 3^1
    # 例:prime_factorization(25)
    # 戻り値: [5, 5]
    # 25 = 5^2
    # 例:prime_factorization(1)
    # 戻り値: []
    # 1 = 1^0
    # 例:prime_factorization(0)
    # 戻り値: []
    # 0 = 0^0
    # 例:prime_factorization(-1)
    # 戻り値: []
    # -1 = -1^0
    # 例:prime_factorization(-24)
    # 戻り値: []
    # -24 = 2^3 * 3^1
    # 例:prime_factorization(-25)
    # 戻り値: []
    # -25 = 5^2
    if n == 0:
        return []
    elif n < 0:
        return []
    else:
        prime_factorization_list = []
        while n % 2 == 0:
            prime_factorization_list.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                prime_factorization_list.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            prime_factorization_list.append(n)
        return prime_factorization_list
