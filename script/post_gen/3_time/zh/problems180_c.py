Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

N = int(input())
divisors = get_divisors(N)
for d in divisors:
    print(d)

=======
Suggestion 2

def cal(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return sorted(res)

n = int(input())
res = cal(n)
for i in res:
    print(i)

=======
Suggestion 3

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if N // i != i:
                print(N // i)
        i += 1

=======
Suggestion 4

def main():
    N = int(input())
    ans = set()
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.add(i)
            ans.add(N//i)
    for i in sorted(ans):
        print(i)

=======
Suggestion 5

def main():
    N=int(input())
    i=1
    while i*i<=N:
        if N%i==0:
            print(i)
            if i!=N//i:
                print(N//i)
        i+=1

=======
Suggestion 6

def prime_factorization(n):
    if n <= 1:
        return []
    prime_factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)
    return prime_factors

n = int(input())
prime_factors = prime_factorization(n)
ans = set([1])
for prime_factor in prime_factors:
    tmp = set()
    for a in ans:
        tmp.add(a)
        tmp.add(a * prime_factor)
    ans = tmp
ans = list(ans)
ans.sort()
for a in ans:
    print(a)

=======
Suggestion 7

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1

=======
Suggestion 8

def p180_c():
    # 1. 问题陈述
    # 我们有N个奶油泡芙。
    # 请找出所有可能的人数，以便在不切割奶油泡芙的情况下将其均匀地分配给这些人。
    #
    # 限制条件
    # 1 ≦ N ≦ 10^{12}
    # N是一个整数。
    #
    # 输入
    # 输入由标准输入提供，格式如下：
    # N
    #
    # 输出
    # 按升序打印人的数量，每个人都在自己的行中。
    #
    # 输入样本 1
    # 6
    #
    # 样本输出 1
    # 1
    # 2
    # 3
    # 6
    # 例如，我们可以把奶油泡芙均匀地分给两个人，每人给三个。
    #
    # 样本输入2
    # 720
    #
    # 样本输出2
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 8
    # 9
    # 10
    # 12
    # 15
    # 16
    # 18
    # 20
    # 24
    # 30
    # 36
    # 40
    # 45
    # 48
    # 60
    # 72
    # 80
    # 90
    # 120
    # 144
    # 180
    # 240
    # 360
    # 720
    #
    # 样本输入3
    # 1000000007
    #
    # 样品输出3
    # 1
    # 1000000007

    # 2. 解题思路
    # 1. 暴力法
    # 2. 求约数
    #

=======
Suggestion 9

def main():
    print("180_c")
    N = int(input())
    i = 1
    while i <= N:
        if N % i == 0:
            print(i)
        i += 1
