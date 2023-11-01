Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def func(n):
    if 2**n > n**2:
        return "Yes"
    else:
        return "No"

=======
Suggestion 2

def main():
    n = int(input())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def power2(n):
    if n == 0:
        return 1
    else:
        return 2 * power2(n-1)

=======
Suggestion 4

def main():
    n = int(input())
    if 2**n > n**2:
        print('Yes')
    else:
        print('No')
