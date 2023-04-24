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
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 5

def main():
    A = [int(x) for x in input().split()]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 6

def main():
    numbers = list(map(int, input().split()))
    if sum(numbers) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 7

def main():
    a = input()
    a = a.split()
    a1 = int(a[0])
    a2 = int(a[1])
    a3 = int(a[2])
    if a1+a2+a3 >= 22:
        print("bust")
    else:
        print("win")
