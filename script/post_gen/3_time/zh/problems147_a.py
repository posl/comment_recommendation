Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = input()
    b = input()
    c = input()
    if int(a) + int(b) + int(c) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    a = input()
    a = a.split(" ")
    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])
    if (a[0] + a[1] + a[2] >= 22):
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    a = input().split()
    sum = 0
    for i in a:
        sum += int(i)
    if sum >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())

    if a+b+c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 6

def main():
    a = input().split()
    sum = 0
    for i in range(3):
        sum += int(a[i])
    if sum >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 7

def main():
    a = input()
    a = a.split(" ")
    a = [int(n) for n in a]
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print('bust')
    else:
        print('win')
