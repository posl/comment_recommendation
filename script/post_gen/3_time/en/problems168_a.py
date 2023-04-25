Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
        print('hon')
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        print('pon')
    else:
        print('bon')

=======
Suggestion 2

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    elif n % 10 == 3:
        print('bon')

=======
Suggestion 3

def main():
    N = int(input())
    if N % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif N % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 4

def main():
    N = int(input())
    if N % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif N % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

=======
Suggestion 5

def main():
    num = input()
    if num[-1] in ['2', '4', '5', '7', '9']:
        print('hon')
    elif num[-1] in ['0', '1', '6', '8']:
        print('pon')
    else:
        print('bon')

=======
Suggestion 6

def main():
    n = int(input())
    r = n % 10
    if r == 3:
        print("bon")
    elif r == 0 or r == 1 or r == 6 or r == 8:
        print("pon")
    else:
        print("hon")

=======
Suggestion 7

def main():
    n = int(input())

    if n == 3:
        print('bon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('hon')

=======
Suggestion 8

def main():
    #input
    N = int(input())
    #output
    if N%10==2 or N%10==4 or N%10==5 or N%10==7 or N%10==9:
        print('hon')
    elif N%10==0 or N%10==1 or N%10==6 or N%10==8:
        print('pon')
    else:
        print('bon')
