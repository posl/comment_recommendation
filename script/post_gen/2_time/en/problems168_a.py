Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
        print("hon")
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print("pon")
    else:
        print("bon")

main()

=======
Suggestion 2

def main():
    N = int(input())
    if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
        print('hon')
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print('pon')
    elif N % 10 == 3:
        print('bon')

=======
Suggestion 3

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
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

main()

=======
Suggestion 5

def main():
    n = int(input())
    if n%10 == 2 or n%10 == 4 or n%10 == 5 or n%10 == 7 or n%10 == 9:
        print("hon")
    elif n%10 == 0 or n%10 == 1 or n%10 == 6 or n%10 == 8:
        print("pon")
    else:
        print("bon")

=======
Suggestion 6

def main():
    N = int(input())
    if N % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif N % 10 in [0, 1, 6, 8]:
        print("pon")
    elif N % 10 == 3:
        print("bon")

=======
Suggestion 7

def main():
    N = int(input())
    if N%10 == 2 or N%10 == 4 or N%10 == 5 or N%10 == 7 or N%10 == 9:
        print('hon')
    elif N%10 == 0 or N%10 == 1 or N%10 == 6 or N%10 == 8:
        print('pon')
    else:
        print('bon')

=======
Suggestion 8

def main():
    n = input()
    if n[-1] in ['2', '4', '5', '7', '9']:
        print 'hon'
    elif n[-1] in ['0', '1', '6', '8']:
        print 'pon'
    else:
        print 'bon'

=======
Suggestion 9

def main():
    N = input()
    if N[-1] in ('2', '4', '5', '7', '9'):
        print('hon')
    elif N[-1] in ('0', '1', '6', '8'):
        print('pon')
    else:
        print('bon')

=======
Suggestion 10

def main():
    #read the input
    n = int(input())
    #find the last digit
    last_digit = n%10
    #print the output
    if last_digit == 2 or last_digit == 4 or last_digit == 5 or last_digit == 7 or last_digit == 9:
        print('hon')
    elif last_digit == 0 or last_digit == 1 or last_digit == 6 or last_digit == 8:
        print('pon')
    else:
        print('bon')
