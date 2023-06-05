Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k,a = map(int, input().split())
    print((k-1+a-1)%n+1)

=======
Suggestion 2

def last_card(n, k, a):
    return (k - (n - a + 1)) % n + 1

=======
Suggestion 3

def main():
    N, K, A = map(int, input().split())
    print((K-1+A-1)%N+1)

=======
Suggestion 4

def main():
    n,k,a = map(int, input().split())
    if k%n == 0:
        print(a)
    else:
        print(a+k%n)

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    print((k - n + a - 1) % n + 1)

=======
Suggestion 6

def main():
    n,k,a = map(int,input().split())
    if k >= n:
        k = k%n
    if a+k > n:
        print(a+k-n)
    else:
        print(a+k)

=======
Suggestion 7

def problem227_a():
    n,k,a = map(int, input().split())
    print((k-1+a-1)%n+1)

=======
Suggestion 8

def main():
    n,k,a = map(int,input().split())
    if k%n == 0:
        print(a)
    else:
        print(k%n)

=======
Suggestion 9

def problem227_a(n,k,a):
    #n个人，k张卡片，第一个人a
    if a == 1:
        return k%n
    else:
        return (k+a-1)%n

=======
Suggestion 10

def main():
    n, k, a = map(int, input().split())
    print((a + k - 1) % n or n)
