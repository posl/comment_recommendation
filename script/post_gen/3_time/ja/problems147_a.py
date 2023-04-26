Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print("bust")
    else:
        print("win")

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
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

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
    a,b,c = map(int,input().split())
    if (a+b+c) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    s = sum(a)
    if s >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 7

def main():
    a_list = list(map(int, input().split()))
    if sum(a_list) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    #input_line = input()
    #a, b, c = input_line.split()
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b + c >= 22:
        print('bust')
    else:
        print('win')
