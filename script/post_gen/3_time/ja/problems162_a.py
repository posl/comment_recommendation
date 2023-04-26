Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    if N[0] == "7" or N[1] == "7" or N[2] == "7":
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
    n = input()
    if '7' in n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = input()
    if '7' in N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def is_included_seven(n):
    while n != 0:
        if n % 10 == 7:
            return True
        n //= 10
    return False

n = int(input())
