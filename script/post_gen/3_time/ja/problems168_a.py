Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
        print("hon")
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        print("pon")
    else:
        print("bon")

=======
Suggestion 2

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
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
    elif N % 10 == 3:
        print("bon")

=======
Suggestion 4

def main():
    N = int(input())
    if N%10 == 2 or N%10 == 4 or N%10 == 5 or N%10 == 7 or N%10 == 9:
        print("hon")
    elif N%10 == 0 or N%10 == 1 or N%10 == 6 or N%10 == 8:
        print("pon")
    else:
        print("bon")

=======
Suggestion 5

def main():
    N = int(input())
    if N%10 == 2 or N%10 == 4 or N%10 == 5 or N%10 == 7 or N%10 == 9:
        print("hon")
    elif N%10 == 0 or N%10 == 1 or N%10 == 6 or N%10 == 8:
        print("pon")
    elif N%10 == 3:
        print("bon")
    else:
        print("error")

=======
Suggestion 6

def main():
    n = int(input())
    l = n % 10
    if l == 2 or l == 4 or l == 5 or l == 7 or l == 9:
        print("hon")
    elif l == 0 or l == 1 or l == 6 or l == 8:
        print("pon")
    elif l == 3:
        print("bon")

=======
Suggestion 7

def main():
    n = int(input())
    if n%10==3:
        print("bon")
    elif n%10==0 or n%10==1 or n%10==6 or n%10==8:
        print("pon")
    else:
        print("hon")

=======
Suggestion 8

def is_hon(n):
    if n % 10 in [2,4,5,7,9]:
        return True
    else:
        return False

=======
Suggestion 9

def get_input():
    n = int(input())
    return n
