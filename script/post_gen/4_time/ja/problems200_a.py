Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 100 == 0:
        print(N // 100)
    else:
        print(N // 100 + 1)

=======
Suggestion 2

def main():
    N = int(input())
    if N % 100 == 0:
        print(int(N / 100))
    else:
        print(int(N / 100) + 1)

=======
Suggestion 3

def getCentury(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100) + 1

=======
Suggestion 4

def main():
    n = int(input())
    print((n + 99) // 100)

=======
Suggestion 5

def main():
    N = int(input())
    print((N - 1) // 100 + 1)

=======
Suggestion 6

def main():
    N = int(input())
    print((N + 99) // 100)

=======
Suggestion 7

def main():
    N = int(input())
    print(int((N+99)/100))

=======
Suggestion 8

def problem200_a(input):
    # 処理を書く
    N = int(input)
    century = N // 100
    if N % 100 == 0:
        return century
    else:
        return century + 1
