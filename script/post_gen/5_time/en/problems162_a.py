Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    if N[0] == '7' or N[1] == '7' or N[2] == '7':
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    if n % 10 == 7 or (n // 10) % 10 == 7 or (n // 100) % 10 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = input()
    if "7" in N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input().strip())
    if n % 10 == 7 or (n // 10) % 10 == 7 or (n // 100) % 10 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def check_seven(number):
    if number % 10 == 7 or (number // 10) % 10 == 7 or number // 100 == 7:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    input = raw_input()
    if "7" in input:
        print "Yes"
    else:
        print "No"

=======
Suggestion 7

def sol():
    n = input()
    if '7' in n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def seven():
    n = input()
    if '7' in n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def contains_7(number):
    if "7" in str(number):
        print("Yes")
    else:
        print("No")
