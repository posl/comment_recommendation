Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    a = sum(map(int, list(str(a))))
    b = sum(map(int, list(str(b))))
    print(a if a > b else b)

=======
Suggestion 3

def getSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num / 10)
    return sum

a, b = map(int, input().split())
print(getSumOfDigits(a) if getSumOfDigits(a) > getSumOfDigits(b) else getSumOfDigits(b))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    a_100 = a // 100
    a_10 = (a - a_100 * 100) // 10
    a_1 = a - a_100 * 100 - a_10 * 10
    b_100 = b // 100
    b_10 = (b - b_100 * 100) // 10
    b_1 = b - b_100 * 100 - b_10 * 10
    a_sum = a_100 + a_10 + a_1
    b_sum = b_100 + b_10 + b_1
    print(max(a_sum, b_sum))

=======
Suggestion 5

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

a, b = map(int, input().split())

print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 6

def main():
    a,b = input().split()
    a_sum = 0
    b_sum = 0
    for i in range(len(a)):
        a_sum += int(a[i])
        b_sum += int(b[i])
    if a_sum > b_sum:
        print(a_sum)
    else:
        print(b_sum)

=======
Suggestion 7

def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

a, b = map(int, input().split())
print(max(sum_digit(a), sum_digit(b)))

=======
Suggestion 8

def main():
    # 標準入力受付
    a, b = map(int, input().split())
    # print(a, b)

    # 処理
    sa = sum(list(map(int, list(str(a)))))
    sb = sum(list(map(int, list(str(b)))))
    if sa > sb:
        print(sa)
    else:
        print(sb)

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    a_sum = 0
    b_sum = 0
    for i in range(3):
        a_sum += a % 10
        a //= 10
        b_sum += b % 10
        b //= 10
    if a_sum > b_sum:
        print(a_sum)
    else:
        print(b_sum)
