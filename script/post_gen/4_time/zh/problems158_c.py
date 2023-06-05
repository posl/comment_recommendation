Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    for i in range(1, 101):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    for i in range(1,101):
        if int(i*0.08) == A and int(i*0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    for p in range(1,1001):
        if int(p * 0.08) == a and int(p * 0.1) == b:
            print(p)
            return
    print(-1)
    return

main()

=======
Suggestion 4

def tax_8(price):
    return int(price * 0.08)

=======
Suggestion 5

def get_price(a, b):
    for i in range(1, 100):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    for i in range(1,1000):
        if int(i*0.08)==A and int(i*0.1)==B:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 7

def get_price(A, B):
    for i in range(1, 101):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1

=======
Suggestion 8

def get_price(A,B):
    for i in range(A,B+1):
        a = int(i*0.08)
        b = int(i*0.1)
        if a == A and b == B:
            return i
    return -1

A,B = map(int,input().split())
print(get_price(A,B))

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    for i in range(1, 100):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)
