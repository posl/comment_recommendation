Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A * B) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A % 2 == 1 and B % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a * b % 2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or (a == 2 and b == 2):
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A == 1 or B == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if (A*B)%2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # A, B = map(int, input().split())
    A, B = map(int, input().split())
    if A * B % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # A, B = map(int, input().split())
    A, B = 3, 1
    if A * B % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    # A, Bの入力
    A, B = map(int, input().split())
    # A, Bの積を2で割った余りが1ならYes、そうでないならNo
    if (A * B) % 2 == 1:
        print('Yes')
    else:
        print('No')
