Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    for i in range(1,10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def solve():
    a,b = map(int,input().split())
    for n in range(1,100000):
        if int(n*0.08) == a and int(n*0.1) == b:
            print(n)
            return
    print(-1)

=======
Suggestion 5

def calc_tax(n, tax):
    return int(n * tax)

A, B = map(int, input().split())
for i in range(1, 1000):
    if calc_tax(i, 0.08) == A and calc_tax(i, 0.1) == B:
        print(i)
        exit()
print(-1)

=======
Suggestion 6

def solve():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    for i in range(1, 10000):
        if (int(i * 0.08) == a) and (int(i * 0.1) == b):
            print(i)
            return
    print(-1)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            exit()
    print(-1)
    return

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    for i in range(1,1000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)
main()

=======
Suggestion 10

def tax(a,b):
    for i in range(1,1000):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1
