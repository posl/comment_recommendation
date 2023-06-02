Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def read_int():
    return int(input())

=======
Suggestion 2

def main():
    n = int(input())
    if n % 10 == 3:
        print("bon")
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        print("pon")
    else:
        print("hon")

=======
Suggestion 3

def main():
    num = int(input())
    num = num % 10
    if num in [2,4,5,7,9]:
        print("hon")
    elif num in [0,1,6,8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 4

def main():
    N = int(input())
    if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
        print("hon")
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print("pon")
    elif N % 10 == 3:
        print("bon")

=======
Suggestion 5

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

=======
Suggestion 6

def main():
    N = input()
    if int(N[-1]) == 2 or int(N[-1]) == 4 or int(N[-1]) == 5 or int(N[-1]) == 7 or int(N[-1]) == 9:
        print("hon")
    elif int(N[-1]) == 0 or int(N[-1]) == 1 or int(N[-1]) == 6 or int(N[-1]) == 8:
        print("pon")
    elif int(N[-1]) == 3:
        print("bon")
    else:
        print("error")

=======
Suggestion 7

def func():
    n = input()
    if n[-1] in ['2','4','5','7','9']:
        print('hon')
    elif n[-1] in ['0','1','6','8']:
        print('pon')
    else:
        print('bon')

=======
Suggestion 8

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 9

def main():
    N = int(input())
    if N%10 in [2,4,5,7,9]:
        print("hon")
    elif N%10 in [0,1,6,8]:
        print("pon")
    else:
        print("bon")
