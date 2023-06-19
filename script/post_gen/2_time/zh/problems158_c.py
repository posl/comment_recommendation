Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    for i in range(1,10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def find_price(A, B):
    for i in range(100):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1

A, B = map(int, input().split())
print(find_price(A, B))

=======
Suggestion 4

def get_price(a, b):
    for i in range(1, 100):
        if (int(i*1.08) == a) and (int(i*1.1) == b):
            return i
    return -1

=======
Suggestion 5

def fun(a,b):
    for i in range(1,100):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1

a,b = map(int,input().split())
print(fun(a,b))

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    for i in range(1,1000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            break
        if i == 999:
            print(-1)

=======
Suggestion 7

def main():
    import sys
    A, B = map(int, sys.stdin.readline().split())
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

main()

=======
Suggestion 8

def solve(a,b):
    for i in range(1,101):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1

a,b = map(int,input().split())
print(solve(a,b))

=======
Suggestion 9

def tax(a,b):
    for i in range(1,101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1
a,b = map(int,input().split())
print(tax(a,b))

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if a == int(i * 0.08) and b == int(i * 0.1):
            print(i)
            exit()
    print(-1)
