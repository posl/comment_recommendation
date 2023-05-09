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
    a, b = map(int, input().split())
    for i in range(1, 1000):
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
            exit()
    print(-1)

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
    for i in range(1, 10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    for i in range(1, 10000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)
main()

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    for i in range(1, 10001):
        if (int(i * 0.08) == a) and (int(i * 0.1) == b):
            print(i)
            return
    print(-1)

=======
Suggestion 8

def calc_price(A, B):
    for i in range(1, 1001):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1

=======
Suggestion 9

def main():
    #A, B = map(int, input().split())
    A, B = 2, 2
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)
