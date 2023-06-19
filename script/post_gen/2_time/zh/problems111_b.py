Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N%111 == 0:
        print(N)
    else:
        print((N//111+1)*111)

=======
Suggestion 2

def main():
    n = int(input())
    if n <= 111:
        print(111)
    elif n <= 222:
        print(222)
    elif n <= 333:
        print(333)
    elif n <= 444:
        print(444)
    elif n <= 555:
        print(555)
    elif n <= 666:
        print(666)
    elif n <= 777:
        print(777)
    elif n <= 888:
        print(888)
    else:
        print(999)

=======
Suggestion 3

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(N, N+1000):
        if i % 111 == 0:
            print(i)
            break

=======
Suggestion 5

def main():
    n = int(input())
    print((n+110)//111*111)

=======
Suggestion 6

def main():
    N = int(input())
    n = N//111
    if N%111 != 0:
        n += 1
    print(n*111)

=======
Suggestion 7

def main():
    n = int(input())
    print(((n+110)//111)*111)

=======
Suggestion 8

def problems111_b():
    n = int(input())
    if n % 111 != 0:
        print((n // 111 + 1) * 111)
    else:
        print(n)

=======
Suggestion 9

def main():
    n = int(input())
    if n == 999:
        print(999)
    else:
        print(n+1)

=======
Suggestion 10

def solve():
    N = int(input())
    print(111 * (N//111 + 1))
