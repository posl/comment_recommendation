Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 2

def buy_cabbage(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y

=======
Suggestion 3

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)

=======
Suggestion 4

def main():
    n,a,x,y = map(int, input().split())
    if n > a:
        print(a*x + (n-a)*y)
    else:
        print(n*x)

=======
Suggestion 5

def problem210_a():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(0, n - a) * y)

=======
Suggestion 6

def calc_cost(N, A, X, Y):
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y

=======
Suggestion 7

def main():
    # Get the input
    input = raw_input().split(" ")
    N = int(input[0])
    A = int(input[1])
    X = int(input[2])
    Y = int(input[3])

    if N <= A:
        print N*X
    else:
        print A*X + (N-A)*Y

=======
Suggestion 8

def calculate_cabbage_price(cabbage_count, cabbage_discount_count, cabbage_price, cabbage_discount_price):
    if cabbage_count > cabbage_discount_count:
        return (cabbage_discount_count * cabbage_price) + ((cabbage_count - cabbage_discount_count) * cabbage_discount_price)
    else:
        return cabbage_count * cabbage_price
