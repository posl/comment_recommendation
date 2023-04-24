Synthesizing 10/10 solutions (Duplicates hidden)

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
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
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

=======
Suggestion 4

def main():
    a, b = list(map(int, input().split()))
    for i in range(1, 1001):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 5

def solve(a,b):
    for i in range(1,10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1

=======
Suggestion 6

def get_price(A, B):
    for price in range(1, 1001):
        if int(price * 0.08) == A and int(price * 0.1) == B:
            return price
    return -1

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    for i in range(1000):
        if (i * 0.08 // 1 == A and i * 0.1 // 1 == B):
            print(i)
            return
    print(-1)

=======
Suggestion 8

def main():
    A,B = map(int, input().split())
    for i in range(1, 1000):
        if A == int(i*0.08) and B == int(i*0.1):
            print(i)
            return
    print(-1)

=======
Suggestion 9

def get_price(a, b):
    price = -1
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            price = i
            break
    return price
