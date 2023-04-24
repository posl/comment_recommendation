Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
        print("hon")
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print("pon")
    elif N % 10 == 3:
        print("bon")

=======
Suggestion 2

def main():
    N = int(input())
    if N%10 == 2 or N%10 == 4 or N%10 == 5 or N%10 == 7 or N%10 == 9:
        print("hon")
    elif N%10 == 0 or N%10 == 1 or N%10 == 6 or N%10 == 8:
        print("pon")
    else:
        print("bon")

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
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
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
    if N[-1] in ["2", "4", "5", "7", "9"]:
        print("hon")
    elif N[-1] in ["0", "1", "6", "8"]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 7

def main():
    N = int(input())
    N = N % 10
    if N in [2, 4, 5, 7, 9]:
        print("hon")
    elif N in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 8

def main():
    N = int(input())
    #print(N)

    if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
        print("hon")
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print("pon")
    elif N % 10 == 3:
        print("bon")
