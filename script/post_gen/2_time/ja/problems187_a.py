Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    A = sum(int(i) for i in str(A))
    B = sum(int(i) for i in str(B))
    if A > B:
        print(A)
    else:
        print(B)

=======
Suggestion 2

def main():
    # 入力
    A, B = map(int, input().split())
    # 処理
    S_A = sum(map(int, list(str(A))))
    S_B = sum(map(int, list(str(B))))
    # 出力
    if S_A >= S_B:
        print(S_A)
    else:
        print(S_B)

=======
Suggestion 3

def sum_num(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

a, b = map(int, input().split())

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    a = sum([int(i) for i in str(a)])
    b = sum([int(i) for i in str(b)])
    print(max(a,b))

=======
Suggestion 5

def sum_digits(n):
    return sum([int(d) for d in str(n)])

A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

=======
Suggestion 6

def main():
    #入力
    A, B = map(int, input().split())
    #出力
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))

=======
Suggestion 7

def sum_digit(num):
    return sum(map(int, str(num)))

A, B = map(int, input().split())
print(max(sum_digit(A), sum_digit(B)))

=======
Suggestion 8

def main():
    A, B = map(int, input().split())

    def S(n):
        return sum(map(int, str(n)))

    print(max(S(A), S(B)))

=======
Suggestion 9

def main():
    input_data = input().split()
    A = int(input_data[0])
    B = int(input_data[1])

    #S(A) = 1 + 2 + 3 = 6
    #S(B) = 2 + 3 + 4 = 9
    #S(A) と S(B) のうち大きい方の値を求めてください。
    #S(A) と S(B) が等しい場合は、S(A) を出力せよ。
    #S(A) = 1 + 2 + 3 = 6
    #S(B) = 2 + 3 + 4 = 9
    #S(A) と S(B) のうち大きい方の値を求めてください。
    #S(A) と S(B) が等しい場合は、S(A) を出力せよ。
    #S(A) = 1 + 2 + 3 = 6
    #S(B) = 2 + 3 + 4 = 9
    #S(A) と S(B) のうち大きい方の値を求めてください。
    #S(A) と S(B) が等しい場合は、S(A) を出力せよ。
    #S(A) = 1 + 2 + 3 = 6
    #S(B) = 2 + 3 + 4 = 9
    #S(A) と S(B) のうち大きい方の値を求めてください。
    #S(A) と S(B) が等しい場合は、S(A) を出力せよ。
    #S(A) = 1 + 2 + 3 = 6
    #S(B) = 2 + 3 + 4 = 9
    #S(A) と S(B) のうち大きい方の値を求めてください。
    #S(A) と S(B) が等しい場合は、S(A) を出力せよ。
    #S(A) = 1 + 2 + 3 = 6
    #S(B

=======
Suggestion 10

def sum_digit(n):
    """nの各桁の和を返す"""
    return sum([int(i) for i in str(n)])
