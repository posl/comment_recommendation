Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N % 10 == 7 or (N // 10) % 10 == 7 or (N // 100) % 10 == 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    if n % 10 == 7 or n // 10 % 10 == 7 or n // 100 == 7:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    if n % 10 == 7 or (n // 10) % 10 == 7 or (n // 100) % 10 == 7:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    if N % 10 == 7 or (N // 10) % 10 == 7 or N // 100 == 7:
        print('Yes')
    else:
        print('No')

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
    N = int(input())
    if "7" in str(N):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    if "7" in str(n):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    num = input()
    if '7' in num:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 9

def main():
    n = int(input())
    print("Yes" if "7" in str(n) else "No")

=======
Suggestion 10

def main():
    # Get input
    n = int(input())
    # Check if 7 is in the number
    if "7" in str(n):
        print("Yes")
    else:
        print("No")
