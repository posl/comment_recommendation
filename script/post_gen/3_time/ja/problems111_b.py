Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N <= 111:
        print(111)
    elif N <= 222:
        print(222)
    elif N <= 333:
        print(333)
    elif N <= 444:
        print(444)
    elif N <= 555:
        print(555)
    elif N <= 666:
        print(666)
    elif N <= 777:
        print(777)
    elif N <= 888:
        print(888)
    elif N <= 999:
        print(999)
    else:
        print('error')

=======
Suggestion 2

def main():
    n = int(input())
    if n < 111:
        print(111)
    elif n < 222:
        print(222)
    elif n < 333:
        print(333)
    elif n < 444:
        print(444)
    elif n < 555:
        print(555)
    elif n < 666:
        print(666)
    elif n < 777:
        print(777)
    elif n < 888:
        print(888)
    else:
        print(999)

=======
Suggestion 3

def main():
    N = int(input())
    if N < 100:
        print(111)
    elif N < 200:
        print(222)
    elif N < 300:
        print(333)
    elif N < 400:
        print(444)
    elif N < 500:
        print(555)
    elif N < 600:
        print(666)
    elif N < 700:
        print(777)
    elif N < 800:
        print(888)
    elif N < 900:
        print(999)
    else:
        print(1111)

=======
Suggestion 4

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 5

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

=======
Suggestion 6

def main():
    N = input()
    if len(set(N)) == 1:
        print(N)
    else:
        print(str(int(N[0])+1)*3)
