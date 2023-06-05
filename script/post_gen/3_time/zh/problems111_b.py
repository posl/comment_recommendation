Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    while n % 111 != 0:
        n += 1
    print(n)

=======
Suggestion 2

def next_abc(n):
    if n%111==0:
        return n
    else:
        return (n//111+1)*111

n=int(input())
print(next_abc(n))

=======
Suggestion 3

def main():
    n = int(input())
    if n%111 == 0:
        print(n)
    else:
        print(n//111*111+111)

=======
Suggestion 4

def get_next_abc(n):
    return (n+110)//111*111

=======
Suggestion 5

def main():
    N = int(input())
    print(N + (111 - N % 111) if N % 111 != 0 else N)

=======
Suggestion 6

def main():
    n = int(input())
    while True:
        if n%111 == 0:
            print(n)
            break
        n += 1

=======
Suggestion 7

def main():
    n = int(input())
    if n%111 == 0:
        print(n)
    else:
        print((n//111+1)*111)

=======
Suggestion 8

def main():
    n = int(input())
    print((n + 110) // 111 * 111)

=======
Suggestion 9

def main():
    n = int(input())
    if n % 111 != 0:
        print(((n // 111) + 1) * 111)
    else:
        print(n)
