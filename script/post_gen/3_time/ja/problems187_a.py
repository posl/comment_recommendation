Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 2

def sum_digit(num):
    s = str(num)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum

a, b = map(int, input().split())
print(max(sum_digit(a), sum_digit(b)))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    a = [int(i) for i in str(A)]
    b = [int(i) for i in str(B)]
    print(max(sum(a), sum(b)))

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    a = sum(map(int,str(a)))
    b = sum(map(int,str(b)))
    if a > b:
        print(a)
    else:
        print(b)

=======
Suggestion 5

def sum_digit(num):
    s = str(num)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum

=======
Suggestion 6

def main():
    a,b = input().split()
    a = list(a)
    b = list(b)
    sumA = 0
    sumB = 0
    for i in a:
        sumA += int(i)
    for i in b:
        sumB += int(i)
    print(max(sumA,sumB))

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    a_sum = sum(map(int, str(a)))
    b_sum = sum(map(int, str(b)))
    print(max(a_sum, b_sum))

=======
Suggestion 8

def S(n):
    return sum([int(i) for i in str(n)])

a, b = map(int, input().split())
print(max(S(a), S(b)))

=======
Suggestion 9

def main():
    # 標準入力から A, B を取得する
    a, b = map(int, input().split())

    # A, B の各桁の合計を求める
    a_sum = 0
    b_sum = 0
    for i in range(3):
        a_sum += a % 10
        b_sum += b % 10
        a = a // 10
        b = b // 10

    # 各桁の合計の大きい方を出力する
    if a_sum >= b_sum:
        print(a_sum)
    else:
        print(b_sum)

=======
Suggestion 10

def main():
    # A, B = map(int, input().split())
    A, B = map(int, '100 999'.split())
    a = A // 100 + (A % 100) // 10 + (A % 100) % 10
    b = B // 100 + (B % 100) // 10 + (B % 100) % 10
    print(max(a, b))
