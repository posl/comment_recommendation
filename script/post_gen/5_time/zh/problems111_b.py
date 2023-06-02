Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    print((N+109)//111*111)

=======
Suggestion 2

def main():
    n = int(input())
    print((n+110)//111*111)

=======
Suggestion 3

def main():
    N = int(input())
    print(N+111-N%111)

=======
Suggestion 4

def abc(n):
    if n%111 == 0:
        return n
    else:
        return (n//111+1)*111

n = int(input())
print(abc(n))

=======
Suggestion 5

def main():
    n = int(input())
    print(111 * ((n + 110) // 111))

=======
Suggestion 6

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n//111+1)*111)

=======
Suggestion 7

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 8

def f(x):
    if x % 111 == 0:
        return x
    else:
        return f(x+1)

N = int(input())
print(f(N))

=======
Suggestion 9

def main():
    n = input()
    if n[0] == n[1] and n[1] == n[2]:
        print(n)
    else:
        print(int(n[0])*111)

=======
Suggestion 10

def abc(n):
    for i in range(111,1000):
        if i >= n:
            return i
