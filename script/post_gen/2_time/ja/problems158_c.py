Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    for i in range(1, 10000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)
main()

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    for i in range(1, 100000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if (i * 0.08 // 1) == a and (i * 0.1 // 1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 7

def solve():
    a,b = map(int,input().split())
    for i in range(1,100):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 8

def calc_tax(price, rate):
    return price * rate // 100

a, b = map(int, input().split())

for i in range(1, 1000):
    if calc_tax(i, 8) == a and calc_tax(i, 10) == b:
        print(i)
        exit()
print(-1)

=======
Suggestion 9

def calc_tax(n):
    return int(n*0.08), int(n*0.1)

=======
Suggestion 10

def get_integer():
    return int(input())
