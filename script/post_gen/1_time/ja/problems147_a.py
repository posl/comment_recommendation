Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A1, A2, A3 = map(int, input().split())
    if A1 + A2 + A3 >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a + b + c <= 21:
        print("win")
    else:
        print("bust")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    if sum(A) > 21:
        print('bust')
    else:
        print('win')

=======
Suggestion 5

def main():
    A1,A2,A3 = map(int,input().split())
    print("win" if A1+A2+A3 <= 21 else "bust")

=======
Suggestion 6

def main():
    a = input().split()
    a = list(map(int, a))
    if sum(a) <= 21:
        print('win')
    else:
        print('bust')

=======
Suggestion 7

def main():
    A = list(map(int, input().split()))
    print('bust' if sum(A) >= 22 else 'win')
