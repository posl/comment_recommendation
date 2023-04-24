Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if int(n) % sum == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N = int(input())
    S = sum(map(int, str(N)))
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 4

def sum_of_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = int(input())
print('Yes' if n % sum_of_digit(n) == 0 else 'No')

=======
Suggestion 5

def main():
    N = int(input())
    S = 0
    while N > 0:
        S += N % 10
        N = N // 10
    if S % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    print("Yes" if N % sum(int(i) for i in str(N)) == 0 else "No")

=======
Suggestion 7

def main():
    n = int(input())
    print("Yes" if n % sum(map(int, str(n))) == 0 else "No")

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    #S(N)を計算
    S = 0
    while N > 0:
        S += N % 10
        N //= 10
    #S(N)で割り切れるか判定
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def sum_of_digits(n):
    return sum(int(c) for c in str(n))

=======
Suggestion 10

def S(N):
    return sum(map(int, str(N)))
