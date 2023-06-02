Synthesizing 10/10 solutions

=======
Suggestion 1

def tax(a,b):
    for i in range(100):
        if int(i*0.08)==a and int(i*0.1)==b:
            return i
    return -1

=======
Suggestion 2

def tax(a,b):
    if a < 1 or a > 100 or a > b:
        return -1
    for i in range(1,100):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1

a,b = input().split()
a = int(a)
b = int(b)
print(tax(a,b))

=======
Suggestion 3

def get_price(A, B):
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()

    print(-1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    for i in range(1,101):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 9

def get_price(a, b):
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1

=======
Suggestion 10

def main():
    a,b = map(int,input().split())
    for i in range(1,10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            exit()
    print(-1)
