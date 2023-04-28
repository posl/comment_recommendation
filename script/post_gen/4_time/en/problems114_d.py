Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors

=======
Suggestion 2

def main():
    N = int(input())
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            D[j] += 1
    print(D.count(75))

main()

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    divisors = [1]
    for i in range(2, N + 1):
        for j in range(len(divisors)):
            divisors.append(divisors[j] * i)
    divisors.sort()
    print(divisors.count(divisors[-1]))

=======
Suggestion 6

def main():
    n = int(input())
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    if divisors == 75:
        print(1)
    else:
        print(0)

=======
Suggestion 7

def main():
    N = int(input())
    divisors = [1]
    for i in range(2, N+1):
        divisors = [x*i for x in divisors]
        divisors = list(set(divisors))
    print(len([x for x in divisors if x % 75 == 0]))

=======
Suggestion 8

def main():
    N = int(input())
    # 約数の数をカウントする
    # 75 = 3^4 * 5^2
    # 75の約数の数は(4+1)*(2+1) = 15個
    # 3^4の約数の数は5個、5^2の約数の数は3個
    # 15 - (5+3) = 7
    # 7個の数字が約数の数になる
    # 75 = 3^4 * 5^2
    # 75の約数の数は(4+1)*(2+1) = 15個
    # 3^4の約数の数は5個、5^2の約数の数は3個
    # 15 - (5+3) = 7
    # 7個の数字が約数の数になる
    ans = 0
    for i in range(1, N+1):
        ans += count_divisors(i)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    #print(n)
    #print("n =", n)
    #print("n! =", factorial(n))
    result = 0
    for i in range(1, factorial(n) + 1):
        if factorial(n) % i == 0:
            #print("i =", i)
            #print("i! =", factorial(i))
            if len(divisors(factorial(i))) == 75:
                result += 1
    print(result)
