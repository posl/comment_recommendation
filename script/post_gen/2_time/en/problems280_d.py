Synthesizing 10/10 solutions

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 2

def main():
    k = int(input())
    if k == 2:
        print(2)
        return
    if k == 3:
        print(3)
        return
    if k == 4:
        print(4)
        return
    if k == 5:
        print(5)
        return
    if k == 6:
        print(9)
        return
    if k == 7:
        print(7)
        return
    if k == 8:
        print(8)
        return
    if k == 9:
        print(9)
        return
    if k == 10:
        print(8)
        return
    if k == 11:
        print(11)
        return
    if k == 12:
        print(12)
        return
    if k == 13:
        print(13)
        return
    if k == 14:
        print(14)
        return
    if k == 15:
        print(15)
        return
    if k == 16:
        print(16)
        return
    if k == 17:
        print(17)
        return
    if k == 18:
        print(18)
        return
    if k == 19:
        print(19)
        return
    if k == 20:
        print(20)
        return
    if k == 21:
        print(21)
        return
    if k == 22:
        print(22)
        return
    if k == 23:
        print(23)
        return
    if k == 24:
        print(24)
        return
    if k == 25:
        print(25)
        return
    if k == 26:
        print(26)
        return
    if k == 27:
        print(27)
        return
    if k == 28:
        print(28)
        return
    if k == 29:
        print(29)
        return
    if k == 30:
        print(30)
        return
    if k == 31:
        print(31)
        return
    if k == 32:
        print(32)
        return
    if k == 33:
        print(33)
        return
    if k == 34:
        print(34)

=======
Suggestion 3

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    if k == 1:
        print(1)
        return
    n = 1
    while True:
        if (10 ** n - 1) % k == 0:
            print(n)
            return
        n += 1

=======
Suggestion 4

def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)

k = int(input())
n = 1
while True:
    if f(n) % k == 0:
        print(n)
        break
    else:
        n += 1

=======
Suggestion 5

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
k=int(input())
n=1
while True:
    if factorial(n)%k==0:
        print(n)
        break
    else:
        n+=1

=======
Suggestion 6

def main():
    k = int(input())
    n = 1
    while True:
        if n % k == 0:
            print(n)
            break
        else:
            n += 1

=======
Suggestion 7

def main():
    k = int(input())
    n = 1
    while True:
        if (n * (n + 1)) % k == 0:
            print(n + 1)
            break
        n += 1

=======
Suggestion 8

def main():
    import math
    K = int(input())
    N = 1
    while True:
        if math.factorial(N) % K == 0:
            print(N)
            exit()
        N += 1

=======
Suggestion 9

def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    else:
        if k == 1:
            print(1)
            return
        else:
            for i in range(1, k):
                if (i * (i + 1)) % k == 0:
                    print(i + 1)
                    return

=======
Suggestion 10

def problem():
    k = int(input())
    n = 1
    while True:
        if n > k:
            print(-1)
            break
        elif (n * (n + 1)) % k == 0:
            print(n + 1)
            break
        n += 1

problem()
