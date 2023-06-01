Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a,b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a*b)
main()

=======
Suggestion 2

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number //= 10
    return result

=======
Suggestion 3

def main():
    k = int(input())
    a,b = map(int,input().split())
    a = int(str(a),k)
    b = int(str(b),k)
    print(a*b)

=======
Suggestion 4

def main():
    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 5

def f(k, a, b):
    a10 = 0
    for i in range(len(a)):
        a10 += int(a[-i-1]) * (k ** i)
    b10 = 0
    for i in range(len(b)):
        b10 += int(b[-i-1]) * (k ** i)
    return a10 * b10

k = int(input())
a, b = input().split()
print(f(k, a, b))

=======
Suggestion 6

def main():
    k = int(input())
    a, b = map(int, input().split())

    print(int(str(a*b), k))

=======
Suggestion 7

def main():
    k = int(input())
    a, b = input().split(" ")
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 8

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a*b)

=======
Suggestion 9

def main():
    base = int(input())
    a, b = map(str, input().split())
    a = int(a, base)
    b = int(b, base)
    print(a*b)
