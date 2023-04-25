Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if i * 0.08 == A and i * 0.1 == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if (i * 0.08) // 1 == A and (i * 0.1) // 1 == B:
            print(i)
            return
    print(-1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    for i in range(1, 10000):
        if (i * 0.08) // 1 == A and (i * 0.1) // 1 == B:
            print(i)
            return
    print(-1)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    for x in range(1, 100000):
        if A == int(x * 0.08) and B == int(x * 0.1):
            print(x)
            return
    print(-1)

=======
Suggestion 7

def tax(a, b):
    for i in range(1, 1000000):
        if (i * 0.08) // 1 == a and (i * 0.1) // 1 == b:
            return i
    return -1

a, b = map(int, input().split())
print(tax(a, b))

=======
Suggestion 8

def main():
    # Put your code here
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 9

def price(A,B):
    for i in range(1,1000):
        if B == int(i*0.1) and A == int(i*0.08):
            return i
    return -1

A,B = map(int,input().split())
print(price(A,B))

=======
Suggestion 10

def main():
    #write your code below this line
    pass
