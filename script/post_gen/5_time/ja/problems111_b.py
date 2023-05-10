Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

=======
Suggestion 2

def main():
    N = int(input())
    if N%111 == 0:
        print(N)
    else:
        print((N//111+1)*111)

=======
Suggestion 3

def main():
    N = int(input())

    if N < 100:
        print(111)
    elif (N >= 100) and (N <= 111):
        print(111)
    elif (N > 111) and (N <= 222):
        print(222)
    elif (N > 222) and (N <= 333):
        print(333)
    elif (N > 333) and (N <= 444):
        print(444)
    elif (N > 444) and (N <= 555):
        print(555)
    elif (N > 555) and (N <= 666):
        print(666)
    elif (N > 666) and (N <= 777):
        print(777)
    elif (N > 777) and (N <= 888):
        print(888)
    elif (N > 888) and (N <= 999):
        print(999)

=======
Suggestion 4

def main():
    n = int(input())
    n_100 = n // 100
    n_10 = (n % 100) // 10
    n_1 = n % 10
    if n_100 == n_10 and n_10 == n_1:
        print(n)
    else:
        if n_100 == 9:
            print(999)
        else:
            print((n_100 + 1) * 100 + (n_100 + 1) * 10 + (n_100 + 1))

=======
Suggestion 5

def main():
    N = int(input())
    while True:
        if N % 111 == 0:
            print(N)
            break
        N += 1

=======
Suggestion 6

def problems111_b():
    n = int(input())
    x = 100
    for i in range(10):
        if n <= x:
            print(x)
            break
        x += 111

=======
Suggestion 7

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N//111)*111+111)

=======
Suggestion 8

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
Suggestion 9

def main():
    N = int(input())
    #print(N)
    #print(type(N))
    #print(N % 111)
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)
    return
