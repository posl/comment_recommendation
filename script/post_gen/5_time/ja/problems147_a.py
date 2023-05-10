Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    if a+b+c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a+b+c <= 21:
        print("win")
    else:
        print("bust")

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    if a+b+c >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 4

def main():
    a = list(map(int,input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 5

def main():
    a = input().split()
    sum = 0
    for i in range(3):
        sum += int(a[i])
    if sum >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print("bust")
    else:
        print("win")
main()

=======
Suggestion 7

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print("bust")
    else:
        print("win")
