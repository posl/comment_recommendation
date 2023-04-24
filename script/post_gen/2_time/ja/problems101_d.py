Synthesizing 10/10 solutions

=======
Suggestion 1

def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 2

def digit_sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 3

def sum_digit(n):
  s = 0
  while n > 0:
    s += n % 10
    n //= 10
  return s

=======
Suggestion 4

def get_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 5

def S(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 6

def f(n):
    return n / sum(map(int, str(n)))

K = int(input())
n = 1
s = [1]
while len(s) < K:
    n += 1
    if f(n) >= f(s[-1]):
        s.append(n)
for i in s:
    print(i)

=======
Suggestion 7

def main():
    K = int(input())

    # すぬけ数を格納するリスト
    snuke = []

    # すぬけ数を求めていく
    for i in range(1, 10):
        snuke.append(i)
    for i in range(10, 10**15+1):
        if i % 10 == 0:
            continue
        if i % sum(map(int, str(i))) == 0:
            snuke.append(i)

    # K 番目までのすぬけ数を出力
    for i in range(K):
        print(snuke[i])

=======
Suggestion 8

def sum_digit(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 9

def sum_digit(n):
    return sum([int(digit) for digit in str(n)])

=======
Suggestion 10

def sum_of_digit(n):
    return sum(map(int, list(str(n))))
