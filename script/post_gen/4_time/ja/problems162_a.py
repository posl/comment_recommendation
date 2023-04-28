Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    if n[0] == "7" or n[1] == "7" or n[2] == "7":
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = input()
    if "7" in n:
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
    N = input()
    if N[0] == '7' or N[1] == '7' or N[2] == '7':
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 5

def main():
    N = input()
    if '7' in N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = input()
    if ("7" in N):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_contain_7(num):
    while num > 0:
        if num % 10 == 7:
            return True
        num //= 10
    return False

=======
Suggestion 8

def check_seven(num):
    num = str(num)
    if '7' in num:
        print('Yes')
    else:
        print('No')
