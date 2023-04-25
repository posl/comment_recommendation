Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    if '7' in N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N = input()
    if "7" in N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    if '7' in str(n):
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 4

def main():
    n = input()
    if "7" in n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    num = int(input())
    if num % 10 == 7 or num // 10 % 10 == 7 or num // 100 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = input()
    if n.find('7') != -1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    inp = input()
    if '7' in inp:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N = input()
    if N[-1] == '7':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    # Read Input
    N = int(input())

    # Check if N contains 7
    if "7" in str(N):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def is_seven(n):
    #convert n to a string
    s = str(n)
    #check if 7 is in the string
    if '7' in s:
        print('Yes')
    else:
        print('No')
