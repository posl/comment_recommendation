Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 4

def main():
    A = [int(i) for i in input().split()]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 5

def main():
    a = [int(x) for x in input().split()]
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 6

def main():
    A = list(map(int,input().split()))
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 7

def main():
    A1, A2, A3 = map(int, input().split())
    if A1+A2+A3 >=22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print('win' if a+b+c < 22 else 'bust')

=======
Suggestion 9

def main():
    line = input().split()
    A = [int(i) for i in line]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")
