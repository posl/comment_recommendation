Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    n = n % 10
    if n == 3:
        print("bon")
    elif n == 0 or n == 1 or n == 6 or n == 8:
        print("pon")
    else:
        print("hon")

=======
Suggestion 2

def get_hon_pon_bon(n):
    if n % 10 in [2, 4, 5, 7, 9]:
        return 'hon'
    elif n % 10 in [0, 1, 6, 8]:
        return 'pon'
    elif n % 10 == 3:
        return 'bon'
    else:
        return 'error'

=======
Suggestion 3

def main():
    n = int(input())
    print("hon" if n%10 in [2,4,5,7,9] else ("pon" if n%10 in [0,1,6,8] else "bon"))

=======
Suggestion 4

def get_honponbon(n):
    honponbon = ""
    if n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
        honponbon = "hon"
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        honponbon = "pon"
    elif n % 10 == 3:
        honponbon = "bon"
    return honponbon

n = int(input())
print(get_honponbon(n))

=======
Suggestion 5

def main():
    N = int(input())
    if N % 10 == 3:
        print("bon")
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print("pon")
    else:
        print("hon")

=======
Suggestion 6

def main():
    a = int(input())
    if a % 10 == 2 or a % 10 == 4 or a % 10 == 5 or a % 10 == 7 or a % 10 == 9:
        print("hon")
    elif a % 10 == 0 or a % 10 == 1 or a % 10 == 6 or a % 10 == 8:
        print("pon")
    else:
        print("bon")

=======
Suggestion 7

def main():
    n = int(input())
    if n % 10 == 3:
        print("bon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("hon")

=======
Suggestion 8

def main():
    n = int(input())
    if n%10 == 2 or n%10 == 4 or n%10 == 5 or n%10 == 7 or n%10 == 9:
        print("hon")
    elif n%10 == 0 or n%10 == 1 or n%10 == 6 or n%10 == 8:
        print("pon")
    else:
        print("bon")

=======
Suggestion 9

def find_hon(n):
    hon_list = [2, 4, 5, 7, 9]
    if n in hon_list:
        return True
    else:
        return False

=======
Suggestion 10

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")
