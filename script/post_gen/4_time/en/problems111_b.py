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
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 3

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(((N // 111) + 1) * 111)

=======
Suggestion 4

def main():
    abc = int(input())
    if abc % 111 == 0:
        print(abc)
    else:
        print((abc // 111 + 1) * 111)

=======
Suggestion 5

def abc111_b():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

abc111_b()

=======
Suggestion 6

def abc111_b():
    n = int(input())
    for i in range(1, 10):
        if n <= i * 111:
            print(i * 111)
            return

=======
Suggestion 7

def abc111_b(n):
    while True:
        if len(set(str(n))) == 1:
            return n
        n += 1

=======
Suggestion 8

def main():
    N = int(input())
    print(111 * ((N // 111) + 1))

=======
Suggestion 9

def main():
    N = int(input())
    print(N+(111-N%111))
