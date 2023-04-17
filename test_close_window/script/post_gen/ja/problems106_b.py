Synthesizing 10/10 solutions (Duplicates hidden)

=======

def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

=======

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1, 2):
        if len([j for j in range(1, i + 1) if i % j == 0]) == 8:
            count += 1
    print(count)

=======

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1, 2):
        if count_divisor(i) == 8:
            count += 1
    print(count)

=======

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1, 2):
        if len([j for j in range(1, i+1) if i % j == 0]) == 8:
            ans += 1
    print(ans)

=======

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1, 2):
        if count_divisor(i) == 8:
            cnt += 1
    print(cnt)

=======

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1, 2):
        if len([j for j in range(1, i+1) if i % j == 0]) == 8:
            cnt += 1
    print(cnt)

=======

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            continue
        if count_divisor(i) == 8:
            count += 1
    print(count)

=======

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        if len([j for j in range(1, i+1) if i % j == 0]) == 8:
            count += 1
    print(count)

=======

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        if len(list(filter(lambda x: i % x == 0, range(1, i+1)))) == 8:
            count += 1
    print(count)
