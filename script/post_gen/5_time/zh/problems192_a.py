Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 2

def coin(X):
    if X%100 == 0:
        return 100
    else:
        return 100 - X%100

=======
Suggestion 3

def get_next_prize_coin(x):
    return (100 - (x % 100)) % 100

=======
Suggestion 4

def extra_coin(x):
    if x % 100 == 0:
        return 100
    else:
        return 100 - x % 100

=======
Suggestion 5

def f(x):
    return 100 - x % 100

=======
Suggestion 6

def main():
    X = int(input())
    if X % 100 == 0:
        print(100)
    else:
        print(100 - X % 100)
    return 0

=======
Suggestion 7

def main():
    x = int(input())
    print(100 - x % 100)
main()

=======
Suggestion 8

def main():
    x = int(input())
    if x % 100 == 0:
        print(100)
    else:
        print(100 - x % 100)
