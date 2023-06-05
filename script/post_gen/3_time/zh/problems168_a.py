Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N%10 in [2,4,5,7,9]:
        print("hon")
    elif N%10 in [0,1,6,8]:
        print("pon")
    else:
        print("bon")

main()

=======
Suggestion 2

def get_pronunciation_of_ben(num):
    if num[-1] == '2' or num[-1] == '4' or num[-1] == '5' or num[-1] == '7' or num[-1] == '9':
        return 'hon'
    elif num[-1] == '0' or num[-1] == '1' or num[-1] == '6' or num[-1] == '8':
        return 'pon'
    elif num[-1] == '3':
        return 'bon'

=======
Suggestion 3

def read_int():
    return int(input())

=======
Suggestion 4

def main():
    n = int(input())
    if n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
        print("hon")
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        print("pon")
    elif n % 10 == 3:
        print("bon")

=======
Suggestion 5

def main():
    n = input()
    n = int(n)
    if n%10 == 2 or n%10 == 4 or n%10 == 5 or n%10 == 7 or n%10 == 9:
        print("hon")
    elif n%10 == 0 or n%10 == 1 or n%10 == 6 or n%10 == 8:
        print("pon")
    elif n%10 == 3:
        print("bon")

=======
Suggestion 6

def main():
    n = int(input())
    if n % 10 in (2, 4, 5, 7, 9):
        print('hon')
    elif n % 10 in (0, 1, 6, 8):
        print('pon')
    else:
        print('bon')

main()

=======
Suggestion 7

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

=======
Suggestion 8

def main():
    num = int(input())
    if num % 10 == 2 or num % 10 == 4 or num % 10 == 5 or num % 10 == 7 or num % 10 == 9:
        print("hon")
    elif num % 10 == 0 or num % 10 == 1 or num % 10 == 6 or num % 10 == 8:
        print("pon")
    elif num % 10 == 3:
        print("bon")

=======
Suggestion 9

def countPronunciation(n):
    n = int(n)
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")
