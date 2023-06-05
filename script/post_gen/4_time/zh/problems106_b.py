Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 2

def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    return count

n = int(input())
count = 0
for i in range(1, n+1):
    if i%2 == 1 and divisors(i) == 8:
        count += 1
print(count)

=======
Suggestion 3

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i ==0:
            return False
        i += 2
    return True

=======
Suggestion 4

def count_divisors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

=======
Suggestion 5

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i==0:
            return False
    return True

=======
Suggestion 6

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    divisors = get_divisors(i)
    if len(divisors) == 8:
        count += 1
print(count)

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 8

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False
    return True

=======
Suggestion 9

def problems106_b():
    #print('问题陈述')
    #print('数字105很特别--它是奇数，但它仍然有八个除数。')
    #print('现在，你的任务是：在1到N（包括）之间有多少个正好有八个正除数的奇数？')
    #print('限制条件')
    #print('N是1到200（包括）之间的一个整数。')
    #print('输入')
    #print('输入由标准输入提供，格式如下：')
    #print('N')
    #print('輸出')
    #print('打印计数。')
    #print('样本输入1')
    #print('105')
    #print('样本输出1')
    #print('1')
    #print('在1到105之间的数字中，唯一一个奇数并且正好有八个除数的数字是105。')
    #print('样本输入2')
    #print('7')
    #print('样本输出2')
    #print('0')
    #print('1有一个除数。3，5和7都是质数，有两个除数。因此，没有满足条件的数字。')
    return
