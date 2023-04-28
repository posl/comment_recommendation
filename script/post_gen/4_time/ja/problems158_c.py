Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    for i in range(1, 10000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    A,B = map(int, input().split())
    for i in range(1,1000):
        if int(i*0.08) == A and int(i*0.1) == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def calc_price(A, B):
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1

A, B = map(int, input().split())
print(calc_price(A, B))

=======
Suggestion 5

def tax(a, b):
    for i in range(1, 1000):
        if (int(i * 0.08) == a) and (int(i * 0.1) == b):
            return i
    return -1

a, b = map(int, input().split())
print(tax(a, b))

=======
Suggestion 6

def get_price():
    a, b = map(int, input().split())
    for i in range(1, 100):
        if (i * 0.08) // 1 == a and (i * 0.1) // 1 == b:
            return i
    return -1

print(get_price())

=======
Suggestion 7

def calculate_tax(price, tax_rate):
    return int(price * tax_rate)

=======
Suggestion 8

def tax_calc(base, tax_rate):
    return base * tax_rate // 100
